import asyncio
from dataclasses import dataclass
from typing import Optional
import os

from openai import OpenAI, RateLimitError


# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@dataclass
class MessageResponse:
    response_text: str
    confidence: float
    suggested_action: str
    channel_formatted_response: str
    error: Optional[str]


SYSTEM_PROMPT = """
You are a telecom customer support AI for an internet and mobile provider.

Responsibilities:
- Help customers resolve connectivity, billing, recharge, and service issues.
- Be clear, polite, and efficient.
- If the issue is serious or unclear, recommend escalation to a human agent.

Channel Rules:
- Voice responses must be under 2 sentences.
- WhatsApp and chat responses can be slightly more detailed.

Always give practical troubleshooting steps if possible.
"""


async def call_openai(prompt: str) -> str:
    """
    Call OpenAI API with a 10-second timeout.
    """

    def api_call():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content

    try:
        return await asyncio.wait_for(
            asyncio.to_thread(api_call),
            timeout=10
        )
    except asyncio.TimeoutError:
        raise TimeoutError("API timeout")


async def handle_message(
    customer_message: str,
    customer_id: str,
    channel: str
) -> MessageResponse:

    # Error case: empty message
    if not customer_message.strip():
        return MessageResponse(
            response_text="",
            confidence=0.0,
            suggested_action="none",
            channel_formatted_response="",
            error="empty_message"
        )

    prompt = f"""
Customer ID: {customer_id}
Channel: {channel}

Customer message:
{customer_message}

Generate a telecom support reply.
"""

    retries = 1

    for attempt in range(retries + 1):

        try:
            ai_text = await call_openai(prompt)

            confidence = 0.85
            suggested_action = "resolve"

            if "cancel" in customer_message.lower():
                suggested_action = "escalate"

            # Format response for channel
            if channel == "voice":
                sentences = ai_text.split(".")
                formatted = ".".join(sentences[:2]).strip()
                if not formatted.endswith("."):
                    formatted += "."
            else:
                formatted = ai_text

            return MessageResponse(
                response_text=ai_text,
                confidence=confidence,
                suggested_action=suggested_action,
                channel_formatted_response=formatted,
                error=None
            )

        except RateLimitError:

            if attempt < retries:
                await asyncio.sleep(2)
                continue

            return MessageResponse(
                response_text="",
                confidence=0.0,
                suggested_action="retry",
                channel_formatted_response="",
                error="rate_limit"
            )

        except TimeoutError:

            return MessageResponse(
                response_text="",
                confidence=0.0,
                suggested_action="retry",
                channel_formatted_response="",
                error="timeout"
            )


# Temporary test function (remove before submission if needed)
async def test():
    result = await handle_message(
        "My internet is not working since morning",
        "CUST123",
        "chat"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(test())
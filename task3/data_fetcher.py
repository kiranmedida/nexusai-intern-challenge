import asyncio
import random
import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class CustomerContext:
    crm_data: Optional[dict]
    billing_data: Optional[dict]
    ticket_history: Optional[dict]
    data_complete: bool
    fetch_time_ms: float


# ---- Mock Systems ----

async def fetch_crm(phone: str):
    await asyncio.sleep(random.uniform(0.2, 0.4))

    return {
        "phone": phone,
        "name": "John Doe",
        "vip": random.choice([True, False])
    }


async def fetch_billing(phone: str):
    await asyncio.sleep(random.uniform(0.15, 0.35))

    # 10% chance of timeout
    if random.random() < 0.1:
        raise TimeoutError("Billing system timeout")

    return {
        "status": random.choice(["paid", "overdue"]),
        "last_payment": "2026-03-01"
    }


async def fetch_ticket_history(phone: str):
    await asyncio.sleep(random.uniform(0.1, 0.3))

    return {
        "recent_tickets": [
            "slow internet",
            "router restart issue",
            "billing confusion"
        ]
    }


# ---- Sequential Fetch ----

async def fetch_sequential(phone: str):

    start = time.perf_counter()

    crm = await fetch_crm(phone)
    billing = await fetch_billing(phone)
    tickets = await fetch_ticket_history(phone)

    end = time.perf_counter()

    fetch_time = (end - start) * 1000

    print(f"Sequential fetch time: {fetch_time:.2f} ms")

    return CustomerContext(
        crm,
        billing,
        tickets,
        True,
        fetch_time
    )


# ---- Parallel Fetch ----

async def fetch_parallel(phone: str):

    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_crm(phone),
        fetch_billing(phone),
        fetch_ticket_history(phone),
        return_exceptions=True
    )

    crm, billing, tickets = results

    data_complete = True

    if isinstance(billing, Exception):
        print("Warning: Billing system failed")
        billing = None
        data_complete = False

    end = time.perf_counter()

    fetch_time = (end - start) * 1000

    print(f"Parallel fetch time: {fetch_time:.2f} ms")

    return CustomerContext(
        crm,
        billing,
        tickets,
        data_complete,
        fetch_time
    )


# ---- Test Runner ----

async def main():

    phone = "9876543210"

    print("\nRunning sequential fetch...")
    await fetch_sequential(phone)

    print("\nRunning parallel fetch...")
    await fetch_parallel(phone)


if __name__ == "__main__":
    asyncio.run(main())
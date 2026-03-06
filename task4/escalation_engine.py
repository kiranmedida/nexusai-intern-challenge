from typing import Tuple


def should_escalate(context, confidence_score: float, sentiment_score: float, intent: str) -> Tuple[bool, str]:
    
    
    if intent == "service_cancellation":
        return True, "service_cancellation"

    
    if confidence_score < 0.65:
        return True, "low_confidence"

    
    if sentiment_score < -0.6:
        return True, "angry_customer"

   
    ticket_history = context.ticket_history.get("recent_tickets", [])
    if ticket_history.count(intent) >= 3:
        return True, "repeat_complaint"

    
    if context.crm_data.get("vip") and context.billing_data:
        if context.billing_data.get("status") == "overdue":
            return True, "vip_overdue"

    
    if context.data_complete is False and confidence_score < 0.80:
        return True, "incomplete_data"

    return False, "ai_can_handle"
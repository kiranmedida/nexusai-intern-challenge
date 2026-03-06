import pytest
from task4.escalation_engine import should_escalate


class MockContext:

    def __init__(self, vip=False, billing_status="paid", tickets=None, data_complete=True):

        self.crm_data = {"vip": vip}
        self.billing_data = {"status": billing_status}
        self.ticket_history = {"recent_tickets": tickets or []}
        self.data_complete = data_complete


def test_rule1_low_confidence():
    """Escalate when AI confidence is below 0.65."""
    ctx = MockContext()
    result = should_escalate(ctx, 0.5, 0.0, "internet_issue")
    assert result == (True, "low_confidence")


def test_rule2_angry_customer():
    """Escalate when sentiment score indicates an angry customer."""
    ctx = MockContext()
    result = should_escalate(ctx, 0.9, -0.8, "internet_issue")
    assert result == (True, "angry_customer")


def test_rule3_repeat_complaint():
    """Escalate when the same complaint appears 3 or more times."""
    ctx = MockContext(tickets=["internet_issue", "internet_issue", "internet_issue"])
    result = should_escalate(ctx, 0.9, 0.0, "internet_issue")
    assert result == (True, "repeat_complaint")


def test_rule4_service_cancellation():
    """Service cancellation requests must always escalate."""
    ctx = MockContext()
    result = should_escalate(ctx, 0.95, 0.0, "service_cancellation")
    assert result == (True, "service_cancellation")


def test_rule5_vip_overdue():
    """VIP customers with overdue billing should escalate."""
    ctx = MockContext(vip=True, billing_status="overdue")
    result = should_escalate(ctx, 0.9, 0.0, "billing_issue")
    assert result == (True, "vip_overdue")


def test_rule6_incomplete_data():
    """Escalate when system data is incomplete and confidence < 0.80."""
    ctx = MockContext(data_complete=False)
    result = should_escalate(ctx, 0.7, 0.0, "internet_issue")
    assert result == (True, "incomplete_data")


def test_edge_case_high_confidence():
    """AI should handle when confidence is high and no rule triggers."""
    ctx = MockContext()
    result = should_escalate(ctx, 0.9, 0.0, "internet_issue")
    assert result == (False, "ai_can_handle")


def test_edge_case_neutral_sentiment():
    """Neutral sentiment and valid data should not escalate."""
    ctx = MockContext()
    result = should_escalate(ctx, 0.85, 0.0, "billing_issue")
    assert result == (False, "ai_can_handle")
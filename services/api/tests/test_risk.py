from app.domain.models import TransferRequest, RiskLevel
from app.domain.risk import TransactionRiskService
from app.infrastructure.demo_history import DemoTransferHistory

def test_new_and_large_transfer_is_high_risk():
    assessment = TransactionRiskService().assess(TransferRequest("demo-user", "new-recipient", 8000), DemoTransferHistory())
    assert assessment.level == RiskLevel.HIGH
    assert assessment.score == 75
    assert len(assessment.reasons) == 2

def test_known_normal_transfer_is_low_risk():
    assessment = TransactionRiskService().assess(TransferRequest("demo-user", "family-member", 500), DemoTransferHistory())
    assert assessment.level == RiskLevel.LOW

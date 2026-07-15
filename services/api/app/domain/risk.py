from .models import RiskAssessment, RiskLevel, TransferRequest
from .ports import TransferHistoryPort

class TransactionRiskService:
    def assess(self, transfer: TransferRequest, history: TransferHistoryPort) -> RiskAssessment:
        score, reasons = 0, []
        if not history.has_recipient(transfer.user_id, transfer.recipient_id):
            score += 40; reasons.append("This recipient is new to you.")
        typical = history.typical_amount(transfer.user_id)
        if typical and transfer.amount > typical * 3:
            score += 35; reasons.append("This amount is much larger than your usual transfers.")
        if history.recent_transfer_count(transfer.user_id) >= 5:
            score += 25; reasons.append("You have made several transfers recently.")
        level = RiskLevel.HIGH if score >= 60 else RiskLevel.MEDIUM if score >= 30 else RiskLevel.LOW
        guidance = "Please verify that you personally know the recipient and that the request is genuine." if score else "This transfer looks consistent with your recent activity. Stay alert for unexpected requests."
        return RiskAssessment(score, level, reasons, guidance)

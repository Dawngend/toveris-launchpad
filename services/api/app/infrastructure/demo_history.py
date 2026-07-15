from ..domain.ports import TransferHistoryPort

class DemoTransferHistory(TransferHistoryPort):
    def has_recipient(self, user_id: str, recipient_id: str) -> bool: return recipient_id == "family-member"
    def recent_transfer_count(self, user_id: str) -> int: return 1
    def typical_amount(self, user_id: str) -> int: return 1500

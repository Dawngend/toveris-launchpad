import hashlib
from datetime import UTC, datetime
from ..domain.models import TransferRequest
from ..domain.ports import LedgerPort

class SimulatedLedger(LedgerPort):
    """Development-only stand-in for Stellar ledger recording."""
    def record_transfer(self, transfer: TransferRequest) -> str:
        payload = f"{transfer.user_id}:{transfer.recipient_id}:{transfer.amount}:{datetime.now(UTC).isoformat()}"
        return "sim_" + hashlib.sha256(payload.encode()).hexdigest()[:16]

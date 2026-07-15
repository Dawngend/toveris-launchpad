from abc import ABC, abstractmethod
from .models import TransferRequest

class TransferHistoryPort(ABC):
    @abstractmethod
    def has_recipient(self, user_id: str, recipient_id: str) -> bool: ...
    @abstractmethod
    def recent_transfer_count(self, user_id: str) -> int: ...
    @abstractmethod
    def typical_amount(self, user_id: str) -> int: ...

class LedgerPort(ABC):
    @abstractmethod
    def record_transfer(self, transfer: TransferRequest) -> str: ...

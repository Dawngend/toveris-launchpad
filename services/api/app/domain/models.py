from dataclasses import dataclass
from enum import StrEnum

class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass(frozen=True)
class TransferRequest:
    user_id: str
    recipient_id: str
    amount: int

@dataclass(frozen=True)
class RiskAssessment:
    score: int
    level: RiskLevel
    reasons: list[str]
    guidance: str

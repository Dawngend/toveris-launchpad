from fastapi import APIRouter
from pydantic import BaseModel, Field
from ..domain.models import TransferRequest
from ..domain.risk import TransactionRiskService
from ..infrastructure.demo_history import DemoTransferHistory

router = APIRouter(prefix="/v1/transfers", tags=["transfers"])

class AssessTransferBody(BaseModel):
    recipient_id: str = Field(min_length=1)
    amount: int = Field(gt=0)

@router.post("/assess")
def assess_transfer(body: AssessTransferBody):
    assessment = TransactionRiskService().assess(TransferRequest("demo-user", body.recipient_id, body.amount), DemoTransferHistory())
    return {"score": assessment.score, "level": assessment.level, "reasons": assessment.reasons, "guidance": assessment.guidance}

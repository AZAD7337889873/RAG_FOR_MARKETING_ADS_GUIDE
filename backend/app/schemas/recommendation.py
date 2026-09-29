from pydantic import BaseModel, Field
from typing import Optional

class RecommendationRequest(BaseModel):
    budget: float = Field(gt=0)
    objective: str = "ROAS"
    platform: Optional[str] = None
    campaign_type: Optional[str] = None
    target_audience: Optional[str] = None
    location: Optional[str] = None

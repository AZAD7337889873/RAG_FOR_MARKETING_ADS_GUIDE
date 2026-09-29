from pydantic import BaseModel, Field
from typing import Optional

class PredictionRequest(BaseModel):
    platform: str
    campaign_type: str = "Display"
    budget: float = Field(gt=0)
    duration_days: int = Field(default=30, gt=0)
    location: Optional[str] = None
    target_audience: Optional[str] = None
    ctr: Optional[float] = None
    conversion_rate: Optional[float] = None

class PredictionResponse(BaseModel):
    predicted_clicks: float
    predicted_conversions: float
    predicted_revenue: float
    predicted_roas: float

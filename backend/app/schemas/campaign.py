from pydantic import BaseModel
from typing import Optional

class Campaign(BaseModel):
    campaign_id: str
    platform: Optional[str] = None
    campaign_type: Optional[str] = None
    target_audience: Optional[str] = None
    location: Optional[str] = None
    budget: float = 0
    spend: float = 0

from pydantic import BaseModel, Field
from typing import Optional

class SimulationRequest(BaseModel):
    current_budget: float = Field(gt=0)
    new_budget: float = Field(gt=0)
    platform: str
    ctr: Optional[float] = None
    conversion_rate: Optional[float] = None
    average_order_value: Optional[float] = 100.0

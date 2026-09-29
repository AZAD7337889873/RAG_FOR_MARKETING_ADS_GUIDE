from sqlalchemy import Column, Integer, String, Float
from backend.app.database.connection import Base

class CampaignDB(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(String, unique=True, index=True)
    platform = Column(String)
    campaign_type = Column(String)
    target_audience = Column(String)
    location = Column(String)
    budget = Column(Float, default=0)
    spend = Column(Float, default=0)
    clicks = Column(Integer, default=0)
    impressions = Column(Integer, default=0)
    conversions = Column(Integer, default=0)
    revenue = Column(Float, default=0)

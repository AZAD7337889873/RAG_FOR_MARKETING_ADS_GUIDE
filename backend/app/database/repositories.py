from sqlalchemy.orm import Session
from backend.app.database.models import CampaignDB

class CampaignRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_campaign_id(self, campaign_id: str):
        return self.db.query(CampaignDB).filter(
            CampaignDB.campaign_id == campaign_id
        ).first()

    def list(self, limit: int = 100):
        return self.db.query(CampaignDB).limit(limit).all()

from fastapi import APIRouter, HTTPException
from backend.app.services.campaign_service import CampaignService

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])
service = CampaignService()

@router.get("")
def get_campaigns(limit: int = 100):
    return service.get_campaigns(limit)

@router.get("/{campaign_id}")
def get_campaign(campaign_id: str):
    campaign = service.get_campaign(campaign_id)
    if campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.get("/summary/overview")
def campaign_summary():
    return service.summary()

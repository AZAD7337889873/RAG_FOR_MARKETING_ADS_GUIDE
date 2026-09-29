from fastapi import APIRouter
from backend.app.schemas.recommendation import RecommendationRequest
from backend.app.services.recommendation_service import RecommendationService

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])
service = RecommendationService()

@router.post("")
def recommend(request: RecommendationRequest):
    return service.recommend(request)

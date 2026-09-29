from backend.app.schemas.recommendation import RecommendationRequest
from backend.app.recommendation.platform import recommend_platform
from backend.app.recommendation.budget import allocate_budget
from backend.app.recommendation.campaign import campaign_recommendations

class RecommendationService:
    def recommend(self, request: RecommendationRequest):
        data = request.model_dump()
        return {
            "platform": recommend_platform(data),
            "budget_allocation": allocate_budget(data["budget"]),
            "campaign_recommendations": campaign_recommendations(data),
        }

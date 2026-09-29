from fastapi import APIRouter
from backend.app.schemas.prediction import PredictionRequest
from backend.app.services.prediction_service import PredictionService

router = APIRouter(prefix="/predictions", tags=["Predictions"])
service = PredictionService()

@router.post("")
def predict(request: PredictionRequest):
    return service.predict(request)

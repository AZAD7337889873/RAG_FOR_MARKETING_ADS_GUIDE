from backend.app.schemas.prediction import PredictionRequest
from backend.app.ml.predictor import Predictor

class PredictionService:
    def __init__(self):
        self.predictor = Predictor()

    def predict(self, request: PredictionRequest):
        return self.predictor.predict(request.model_dump())

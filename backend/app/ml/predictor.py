from backend.app.ml.features import build_features
from backend.app.ml.model_loader import ModelLoader

class Predictor:
    def __init__(self):
        self.loader = ModelLoader()

    def _model_predict(self, filename, features):
        model = self.loader.load(filename)
        if model is None:
            return None
        try:
            # Trained models can adapt this section to their exact feature order.
            return float(model.predict([list(features.values())])[0])
        except Exception:
            return None

    def predict(self, data: dict):
        f = build_features(data)
        budget = f["budget"]

        clicks = self._model_predict("click_model.pkl", f)
        conversions = self._model_predict("conversion_model.pkl", f)
        revenue = self._model_predict("revenue_model.pkl", f)
        roas = self._model_predict("roas_model.pkl", f)

        # Baseline fallback keeps the API usable before models are trained.
        clicks = clicks if clicks is not None else budget * 20
        conversions = conversions if conversions is not None else clicks * 0.03
        revenue = revenue if revenue is not None else conversions * 100
        roas = roas if roas is not None else revenue / budget if budget else 0

        return {
            "predicted_clicks": round(max(clicks, 0), 2),
            "predicted_conversions": round(max(conversions, 0), 2),
            "predicted_revenue": round(max(revenue, 0), 2),
            "predicted_roas": round(max(roas, 0), 4),
        }

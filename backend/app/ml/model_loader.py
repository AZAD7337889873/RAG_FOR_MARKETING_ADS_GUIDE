from pathlib import Path
import joblib
from backend.app.config.settings import settings

class ModelLoader:
    def load(self, model_name: str):
        path = Path(settings.ml_models_path) / model_name
        if not path.exists():
            return None
        try:
            return joblib.load(path)
        except Exception:
            return None

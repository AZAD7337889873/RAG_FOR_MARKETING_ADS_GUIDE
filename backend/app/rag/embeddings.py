try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None

from backend.app.config.settings import settings

class EmbeddingService:
    def __init__(self):
        self.model = None
        if SentenceTransformer:
            try:
                self.model = SentenceTransformer(settings.embedding_model)
            except Exception:
                self.model = None

    def embed(self, texts):
        if not self.model:
            return []
        return self.model.encode(texts).tolist()

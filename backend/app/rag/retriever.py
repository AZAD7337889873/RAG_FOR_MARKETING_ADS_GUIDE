from backend.app.rag.documents import load_documents
from backend.app.rag.vector_store import VectorStore

class Retriever:
    def __init__(self):
        self.store = VectorStore(load_documents())

    def retrieve(self, query: str, top_k: int = 5):
        return self.store.search(query, top_k)

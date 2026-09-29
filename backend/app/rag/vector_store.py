from pathlib import Path

class VectorStore:
    """Lightweight local document store.

    This is intentionally simple. Chroma can be added here later without
    changing the API/service layer.
    """

    def __init__(self, documents=None):
        self.documents = documents or []

    def add_documents(self, documents):
        self.documents.extend(documents)

    def search(self, query: str, top_k: int = 5):
        terms = set(query.lower().split())

        scored = []
        for doc in self.documents:
            text = doc.get("text", "").lower()
            score = sum(1 for term in terms if term in text)
            if score:
                scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored[:top_k]]

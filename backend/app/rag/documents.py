from pathlib import Path
from backend.app.config.settings import settings

def load_documents():
    root = Path(settings.knowledge_base_path)
    documents = []

    if not root.exists():
        return documents

    for path in root.rglob("*.txt"):
        documents.append({
            "source": str(path.relative_to(root)),
            "text": path.read_text(encoding="utf-8"),
        })

    return documents

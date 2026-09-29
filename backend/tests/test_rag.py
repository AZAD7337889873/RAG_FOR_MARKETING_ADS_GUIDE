from backend.app.rag.retriever import Retriever

def test_retriever():
    retriever = Retriever()
    results = retriever.retrieve("budget optimization")
    assert isinstance(results, list)

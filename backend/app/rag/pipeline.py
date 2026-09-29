from backend.app.rag.retriever import Retriever
from backend.app.rag.prompts import SYSTEM_PROMPT
from backend.app.llm.ollama import OllamaClient

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = OllamaClient()

    def ask(self, question: str, top_k: int = 5):
        docs = self.retriever.retrieve(question, top_k)

        context = "\n\n".join(
            f"[Source: {doc['source']}]\n{doc['text']}"
            for doc in docs
        )

        prompt = f"""
{SYSTEM_PROMPT}

Knowledge-base context:
{context or "No matching knowledge-base documents were found."}

User question:
{question}

Answer using the context where relevant. If the context is insufficient, say what is missing.
"""

        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "sources": [{"source": d["source"]} for d in docs],
        }

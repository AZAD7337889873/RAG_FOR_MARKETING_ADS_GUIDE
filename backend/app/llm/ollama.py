import requests
from backend.app.config.settings import settings
from backend.app.llm.base import LLMClient

class OllamaClient(LLMClient):
    def __init__(self):
        self.base_url = settings.ollama_base_url.rstrip("/")
        self.model = settings.ollama_model

    def generate(self, prompt: str) -> str:
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=300,
            )
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.RequestException as exc:
            return (
                "Ollama is not available. Start Ollama and make sure the "
                f"'{self.model}' model is installed. Technical detail: {exc}"
            )

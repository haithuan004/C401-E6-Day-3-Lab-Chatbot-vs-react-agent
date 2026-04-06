from typing import Dict, Any

from src.core.llm_provider import LLMProvider
from src.telemetry.metrics import tracker


class BaselineChatbot:
    """Simple one-shot chatbot baseline without tools or iterative reasoning."""

    def __init__(self, llm: LLMProvider):
        self.llm = llm

    def get_system_prompt(self) -> str:
        return (
            "You are a helpful chatbot assistant. "
            "Answer directly in Vietnamese. "
            "Do not use tools and do not mention internal reasoning."
        )

    def run(self, user_input: str) -> Dict[str, Any]:
        result = self.llm.generate(user_input, system_prompt=self.get_system_prompt())
        tracker.track_request(
            provider=result.get("provider", "unknown"),
            model=self.llm.model_name,
            usage=result.get("usage", {}),
            latency_ms=result.get("latency_ms", 0),
        )
        return result

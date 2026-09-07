import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()


def get_llm(
    context_size: int = 8192,
    num_predict: int = 1024,
) -> ChatOllama:
    """Agent별 설정으로 Ollama 모델을 생성한다."""

    base_url = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434",
    )

    model = os.getenv(
        "OLLAMA_MODEL",
        "qwen2.5-coder:14b",
    )

    temperature = float(
        os.getenv("LLM_TEMPERATURE", "0")
    )

    return ChatOllama(
        base_url=base_url,
        model=model,
        temperature=temperature,
        num_ctx=context_size,
        num_predict=num_predict,
    )

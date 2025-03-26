from config import config
from langchain_ollama.llms import OllamaLLM


ollama_model = (
    OllamaLLM(**config.get_llm_config("ollama"))
    if config.is_enabled("ollama")
    else None
)

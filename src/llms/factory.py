from config import CONFIG
from .akash import AkashLLM
from .ollama import OllamaLLM


def get_llm(llm):
    if llm == "ollama":
        ollama_config = CONFIG.llm_config["ollama"]
        return OllamaLLM(**ollama_config)
    elif llm == "akash":
        akash_config = CONFIG.llm_config["akash"]
        return AkashLLM(**akash_config)

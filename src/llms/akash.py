from langchain_openai import ChatOpenAI
from langchain.llms.base import LLM
from langchain_openai import ChatOpenAI


class AkashLLM(ChatOpenAI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, prompt, stop=None):
        return f"AkashLLM Response to: {prompt}"

    @property
    def _identify_params(self):
        return {
            "api_key": self.openai_api_key,
            "base_url": self.openai_api_base,
            "model": self.model_name,
            "temperature": self.temperature,
        }

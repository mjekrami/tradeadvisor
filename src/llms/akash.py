from config import config
from langchain_openai import ChatOpenAI

api_key = config.get_llm_config("akash", "akash_key")
temperature = config.get_llm_config("akash", "model_temperature")
base_url = config.get_llm_config("akash", "akash_base_url")
model = config.get_llm_config("akash", "akash_model")


akash_llm = ChatOpenAI(
    temperature=0 if not temperature else temperature,
    api_key=api_key,
    base_url=base_url,
    model=model,
)

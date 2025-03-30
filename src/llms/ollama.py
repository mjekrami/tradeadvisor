from langchain_ollama import ChatOllama


class OllamaLLM(ChatOllama):
    def __init__(self, *args, **kwargs):
        super(OllamaLLM, self).__init__(*args, **kwargs)
        self.base_url = kwargs.get("base_url", "localhost:11434")
        self.model = kwargs.get("model", None)
        self.temperature = kwargs.get("temperature", 0)

    def __call__(self, prompt, stop=None):
        return f"OllamaLLM Response to: {prompt}"

    @property
    def _identify_params(self):
        return self.__dict__

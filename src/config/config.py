import os
import yaml


class Config:
    def __init__(self):
        config = self._load_config()
        self.llm_config = config.get("llms")
        self.agent_config = config.get("agents")
        self.tool_config = config.get("tools")

    def _load_config(self):
        if os.path.exists("config.yaml"):
            file_path = "config.yaml"
        else:
            file_path = "config.yml"

        with open(file_path) as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as e:
                print(f"Error occured: {str(e)}")
                return
        return config


CONFIG = Config()

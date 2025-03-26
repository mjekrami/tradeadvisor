import os
import logging
import yaml

logger = logging.getLogger(__name__)

if os.path.exists("config.yaml"):
    config_file = "config.yaml"
else:
    config_file = "config.yml"

with open(config_file) as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as error:
        logger.error(error)


def get_llm_config(llm, key):
    if llm is not None:
        return config["llms"][llm][key]
    return config["llms"][llm]


def is_enabled(key):
    return config[key]["enabled"]


def get_tools_config(tool, key):
    if tool is not None:
        return config["tools"][tool][key]

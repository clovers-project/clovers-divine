from pydantic import BaseModel
from clovers.config import config as clovers_config


class Config(BaseModel):
    font: str = "data/fortune/resource/font/sakura.ttf"
    resorce_path: str = "data/fortune/resource"
    output_path: str = "data/fortune/output"


config_key = __package__
config = Config.model_validate(clovers_config.get(config_key, {}))
clovers_config[config_key] = config.model_dump()

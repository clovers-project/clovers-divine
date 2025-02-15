from pydantic import BaseModel
from clovers.config import config as clovers_config


class Config(BaseModel):
    daily_fortune_data: str = "data/fortune/daily"
    daily_fortune_resorce: str = "data/fortune/daily/basemap/"
    daily_fortune_title_font: str = "data/fortune/daily/font/Mamelon.otf"
    daily_fortune_text_font: str = "data/fortune/daily/font/sakura.ttf"
    tarot_resource: str = "data/fortune/tarot"


config_key = __package__
config = Config.model_validate(clovers_config.get(config_key, {}))
clovers_config[config_key] = config.model_dump()

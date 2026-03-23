from clovers.config import Config as CloversConfig
from pydantic import BaseModel


class Config(BaseModel):
    daily_fortune_data: str = "data/divine/daily_fortune"
    daily_fortune_resorce: str = "data/divine/daily_fortune/basemap/"
    daily_fortune_title_font: str = "data/divine/daily_fortune/font/Mamelon.otf"
    daily_fortune_text_font: str = "data/divine/daily_fortune/font/sakura.ttf"
    tarot_resource: str = "data/divine/tarot"
    tarot_merge_forward: bool = False

    @classmethod
    def sync_config(cls):
        """获取 `CloversConfig.environ()[__package__]` 配置并将默认配置同步到全局配置中。"""
        __config_dict__: dict = CloversConfig.environ().setdefault(__package__, {})
        __config_dict__.update((__config__ := cls.model_validate(__config_dict__)).model_dump())
        return __config__

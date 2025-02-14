from .config import config as fortune_config
from .clovers import plugin, Event, Result
from .daily import Manager as FortuneManager


fortune_manager = FortuneManager(
    path=fortune_config.path,
    resource_path=fortune_config.daily_fortune_resorce,
    title_font=fortune_config.daily_fortune_title_font,
    text_font=fortune_config.daily_fortune_text_font,
)


@plugin.handle(["今日运势", "抽签", "运势"], ["group_id", "user_id"])
async def _(event: Event):
    group_id = event.group_id
    user_id = event.user_id
    if result := fortune_manager.get_results(user_id):
        text = "你今天抽过签了，再给你看一次哦🤗"
        image = fortune_manager.cache(group_id, user_id) or fortune_manager.draw(group_id, user_id, result)
    else:
        text = "✨今日运势✨"
        image = fortune_manager.draw(group_id, user_id, fortune_manager.divine(user_id))
    return [Result("at", user_id), text, image]


@plugin.handle("塔罗牌")
async def _(event: Event):
    return


@plugin.handle("占卜")
async def _(event: Event):
    return


__plugin__ = plugin

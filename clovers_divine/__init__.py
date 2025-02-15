import asyncio
from .config import config as fortune_config
from .clovers import plugin, Event, Result
from .daily_fortune import Manager as FortuneManager
from .tarot import Manager as TarotManager

fortune_manager = FortuneManager(
    data_path=fortune_config.daily_fortune_data,
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


tarot_manager = TarotManager(resource_path=fortune_config.tarot_resource)


@plugin.handle(["塔罗牌"], ["user_id"])
async def _(event: Event):
    info, pic, flag = tarot_manager.tarot()
    theme = tarot_manager.random_theme()
    image = tarot_manager.draw(theme, pic, flag)
    return [Result("at", event.user_id), f"回应是{info}", image]


if fortune_config.tarot_merge_forward:
    send_tarot_divine = "merge_forward"
else:
    send_tarot_divine = "list"


@plugin.handle(["占卜"], ["user_id"])
async def _(event: Event):
    tips, result_list = tarot_manager.divine()
    await event.send(f"启动{tips}，正在洗牌中...")
    theme = tarot_manager.random_theme()
    result = []
    for info, pic, flag in result_list:
        image = tarot_manager.draw(theme, pic, flag)
        if image:
            result.append(Result("list", [Result("text", info), Result("image", image)]))
        else:
            result.append(Result("text", info))
    return Result(send_tarot_divine, result)


__plugin__ = plugin

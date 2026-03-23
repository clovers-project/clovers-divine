from clovers import Plugin, Result
from .clovers import Event, build_result, send_merge_forward, send_segmented
from .daily_fortune import Manager as FortuneManager
from .tarot import Manager as TarotManager
from .config import Config

__plugin__ = plugin = Plugin(build_result=build_result, priority=10, block=False)
__plugin__.set_protocol("properties", Event)
__config__ = Config.sync_config()


fortune_manager = FortuneManager(
    __config__.daily_fortune_data,
    __config__.daily_fortune_resorce,
    __config__.daily_fortune_title_font,
    __config__.daily_fortune_text_font,
)
tarot_manager = TarotManager(__config__.tarot_resource)

if __config__.tarot_merge_forward:
    send_tarot_divine = send_merge_forward
else:
    send_tarot_divine = send_segmented


@plugin.handle(["今日运势", "抽签", "运势"], ["group_id", "user_id"], block=(True, True))
async def _(event: Event):
    user_id = event.user_id
    group_id = event.group_id or f"private:{user_id}"
    if image := fortune_manager.cache(group_id, user_id):
        text = "你今天在本群已经抽过签了，再给你看一次哦🤗"
    elif result := fortune_manager.get_results(user_id):
        text = "你今天已经抽过签了，再给你看一次哦🤗"
        image = fortune_manager.draw(group_id, user_id, result)
    else:
        text = "✨今日运势✨"
        result = fortune_manager.divine(user_id)
        image = fortune_manager.draw(group_id, user_id, result)
    return [Result("at", user_id), text, image]


@plugin.handle(["塔罗牌"], ["user_id", "nickname"])
async def _(event: Event):
    card, explain, pic, flag = tarot_manager.tarot()
    if "extra_context" not in event.properties:
        event.properties["extra_context"] = []
    event.extra_context.append(f"[系统提示]{event.nickname}占卜的结果为 {card} 请解读。")
    theme = tarot_manager.random_theme()
    image = tarot_manager.draw(theme, pic, flag)
    return [Result("at", event.user_id), f"回应是{card}{explain}", image]


@plugin.handle(["占卜"], ["user_id", "nickname"])
async def _(event: Event):
    tips, tarot_result_list = tarot_manager.divine()
    await event.call("text", f"启动{tips}，正在洗牌中...")
    theme = tarot_manager.random_theme()
    result_list = []
    infos = []
    for info, explain, pic, flag in tarot_result_list:
        infos.append(info)
        image = tarot_manager.draw(theme, pic, flag)
        if image:
            result_list.append(Result("list", [Result("text", f"{info}{explain}"), Result("image", image)]))
        else:
            result_list.append(Result("text", f"{info}{explain}"))
    if "extra_context" not in event.properties:
        event.properties["extra_context"] = []
    event.extra_context.append(f"[系统提示]{event.nickname}占卜的结果为 {",".join(infos)} 请解读。")
    return send_tarot_divine(result_list)

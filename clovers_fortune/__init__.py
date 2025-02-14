from .config import config as fortune_config
from .clovers import plugin, Event, Result
from .core import manager


@plugin.handle(["今日运势", "抽签", "运势"], ["group_id", "user_id"])
async def _(event: Event):
    group_id = event.group_id
    user_id = event.user_id
    image = manager.cache(group_id, user_id)
    if image:
        text = "你今天抽过签了，再给你看一次哦🤗"
    else:
        if user_id in manager.results:
            text = "你今天抽过签了，再给你看一次哦🤗"
            result = manager.results[user_id]
        else:
            text = "✨今日运势✨"
            result = manager.divine(user_id)
        image = manager.draw(result, event.group_id)
    return [Result("at", user_id), text, image]


@plugin.handle("塔罗牌")
async def _(event: Event):
    return


@plugin.handle("占卜")
async def _(event: Event):
    return


from pathlib import Path
from clovers.logger import logger
from clovers_apscheduler import scheduler

output_path = Path(fortune_config.output_path)


# 清空昨日生成的图片
@scheduler.scheduled_job("cron", hour=0, minute=0, misfire_grace_time=60)
async def _():
    for group_path in output_path.iterdir():
        for pic in group_path.iterdir():
            pic.unlink()
    logger.info("运势图片缓存已清空")

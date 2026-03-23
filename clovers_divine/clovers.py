import asyncio
from io import BytesIO
from clovers import EventProtocol, Result
from typing import Protocol, Literal, overload


class Event(EventProtocol, Protocol):
    user_id: str
    group_id: str | None
    nickname: str
    extra_context: list[str]

    @overload
    async def call(self, key: Literal["text"], message: str): ...

    @overload
    async def call(self, key: Literal["image"], message: BytesIO | bytes): ...

    @overload
    async def call(self, key: Literal["list"], message: list[Result]): ...


def build_result(result):
    if isinstance(result, Result):
        return result
    if isinstance(result, str):
        return Result("text", result)
    if isinstance(result, BytesIO):
        return Result("image", result)
    if isinstance(result, list):
        return Result("list", [build_result(seg) for seg in result if seg])


def send_merge_forward(result_list: list[Result]) -> Result:
    return Result("merge_forward", result_list)


def send_segmented(result_list: list[Result]) -> Result:
    async def segmented_result(result_list: list[Result]):
        for result in result_list:
            yield result
            await asyncio.sleep(2)

    return Result("segmented", segmented_result(result_list))

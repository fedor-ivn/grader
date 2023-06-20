from typing import AsyncGenerator
from asyncio import Future
from io import BytesIO
from typing import List


async def cache_stream(stream: BytesIO) -> AsyncGenerator[bytes, None]:
    chunks: List[bytes] = []
    has_finished = False

    notify_waiter: Future[None]
    wait_for_data = Future()
    notify_waiter = wait_for_data

    def on_data(chunk: bytes) -> None:
        chunks.append(chunk)
        notify_waiter.set_result(None)
        new_wait_for_data = Future()
        nonlocal notify_waiter
        notify_waiter = new_wait_for_data
        wait_for_data = new_wait_for_data

    def on_end() -> None:
        nonlocal has_finished
        has_finished = True
        notify_waiter.set_result(None)

    stream.subscribe(on_data, on_end)

    while True:
        if chunks:
            yield chunks.pop(0)
            continue
        if has_finished:
            break
        await wait_for_data
    stream.unsubscribe(on_data, on_end)

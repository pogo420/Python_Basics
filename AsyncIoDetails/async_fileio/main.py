from asyncio import Queue, AbstractEventLoop
from signal import SIGINT, SIGTERM, SIGHUP
from typing import List
import aiofiles
from aiohttp import ClientSession
import asyncio
import time
import uvloop


async def shutdown(signal: int, loop: AbstractEventLoop):
    """Function for graceful shutdown"""
    print(f"Shutting down.., received signal:{signal}")
    # collecting tasks
    tasks = [task for task in asyncio.all_tasks() if task != asyncio.current_task()]
    # cancelling tasks
    [task.cancel() for task in tasks]
    print(f"cancelling {len(tasks)} pending tasks..")
    # waiting for cancel activity to close.
    await asyncio.gather(*tasks, return_exceptions=True)  # if return_exception is not set it will be handled by
    # global exception handler
    loop.stop()


def exception_handler(loop, context: dict):
    print(f"""Error:{context.get("exception")}""")


async def get_data(file_name: str, queue_):
    """Function to read file in async mode and save data into Queue"""
    async with aiofiles.open(file_name) as fptr:
        line: str
        async for line in fptr:
            print(f"putting data:{line.strip()} to queue")
            await queue_.put(line.strip())
            # await asyncio.sleep(0.2)


async def server_request(session: ClientSession, url: str):
    """Function for async http request"""
    request_data: str
    async with session.get(url) as request:
        request_data = await request.text()
    print(f"response from server:{request_data}")


async def server_helper(base_url: str, queue_):
    """Function for orchestrating async http call"""
    results_: List[str]

    async with ClientSession() as session:  # creating client session
        while True:
            task: str = await queue_.get()
            url: str = base_url.replace("{{user}}", task.strip())
            print(f"making api call for url:{url}")
            asyncio.create_task(server_request(session, url))  # creating background tasks
            queue_.task_done()


async def main():
    base_url_: str = "http://127.0.0.1:5000/?user={{user}}"

    loop: AbstractEventLoop = asyncio.get_event_loop()

    for s in (SIGINT, SIGTERM, SIGHUP):
        loop.add_signal_handler(s,
                                lambda s=s: asyncio.create_task(shutdown(s, loop)))

    loop.set_exception_handler(exception_handler)  # global exception handler

    queue = Queue()
    loop.create_task(get_data("inp.txt", queue))
    await loop.create_task(server_helper(base_url_, queue))


if __name__ == '__main__':
    t_init = time.time()
    uvloop.install()  # to enable uv loop
    asyncio.run(main())
    print(f"{time.time() - t_init} seconds")

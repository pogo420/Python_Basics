
from asyncio import Task
from typing import List, Awaitable
import time
import requests
from aiohttp import ClientSession
from requests import Response
import concurrent.futures
import asyncio
import uvloop


async def async_task_handler(session: ClientSession, url: str) -> str:
    """Function for async http request"""
    request_data: str
    async with session.get(url) as request:
        request_data = await request.text()
    return request_data


async def async_process(base_url: str, tasks_: List[str]) -> List[str]:
    """Function for orchestrating async http call"""
    results_: List[str]
    async_tasks: List[Task] = []

    async with ClientSession() as session:  # creating client session
        for task in tasks_:
            url: str = base_url.replace("{{user}}", task)
            async_tasks.append(asyncio.create_task(async_task_handler(session, url)))  # creating background tasks
        results_ = await asyncio.gather(*async_tasks)
    return results_


def task_handler(url: str) -> str:
    """Handling synchronous api request"""
    response: Response = requests.get(url)
    return response.text


async def converting_blocker_to_non_blocker(base_url: str, tasks_: List[str]) -> List[str]:
    """Function to convert blocking to non blocking"""
    results_: List[str]
    async_tasks: List[Awaitable] = []
    loop = asyncio.get_event_loop()

    for task in tasks_:
        url: str = base_url.replace("{{user}}", task)
        async_tasks.append(
                loop.run_in_executor(None, task_handler, url)  # executing blocking calls in loop
        )
    results_ = await asyncio.gather(*async_tasks)
    return results_


def sync_request(base_url: str, tasks_: List[str]) -> List[str]:
    """Function to implement synchronous request"""
    results_: List[str] = []
    for task in tasks_:
        url: str = base_url.replace("{{user}}", task)
        results_.append(task_handler(url))
    return results_


def multi_threads(base_url: str, tasks_: List[str]) -> List[str]:
    """Function to implement multi threads"""
    results_: List[str]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        url: List[str] = list(map(lambda task: base_url.replace("{{user}}", task), tasks_))
        temp_ = executor.map(task_handler, url)
        results_ = list(temp_)
        return results_


def multi_process(base_url: str, tasks_: List[str]) -> List[str]:
    """Function to implement multi threads"""
    results_: List[str]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        url: List[str] = list(map(lambda task: base_url.replace("{{user}}", task), tasks_))
        temp_ = executor.map(task_handler, url)
        results_ = list(temp_)
        return results_


if __name__ == '__main__':
    base_url_: str = "http://127.0.0.1:5000/?user={{user}}"
    tasks: List[str] = ["arnab", "arnablovespython", "ola", "user", "async", "sync", "concurrent", "23iioi32"]

    t_init = time.time()
    results = sync_request(base_url_, tasks)
    print(f"Results: {results}, it took {time.time()-t_init} seconds via sync approach")

    t_init = time.time()
    results = multi_threads(base_url_, tasks)
    print(f"Results: {results}, it took {time.time()-t_init} seconds via Multi thread pool approach")

    t_init = time.time()
    results = multi_process(base_url_, tasks)
    print(f"Results: {results}, it took {time.time()-t_init} seconds via Multi process pool approach")

    t_init = time.time()
    results = asyncio.run(async_process(base_url_, tasks))
    print(f"Results: {results}, it took {time.time() - t_init} seconds via AsyncIO+aiohttp process approach")

    t_init = time.time()
    results = asyncio.run(converting_blocker_to_non_blocker(base_url_, tasks))
    print(f"Results: {results}, it took {time.time() - t_init} seconds via run in loop executor process approach "
          f"converting blocking to non blocking")

    t_init = time.time()
    # uvloop.install()
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    results = asyncio.run(async_process(base_url_, tasks))

    print(f"Results: {results}, it took {time.time() - t_init} seconds via AsyncIO+aiohttp+uvloop process approach")
import asyncio
import aiohttp

async def async_task_handler(session, url: str) -> str:
    request_data:str
    async with session.get(url) as request:
        request_data = await request.text
    return request_data


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        tasks.append(asyncio.create_task(async_task_handler()))
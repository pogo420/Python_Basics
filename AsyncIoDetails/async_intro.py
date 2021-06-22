import asyncio
import time
from datetime import datetime
from random import randint


def current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


def sync_intermediate_call():
    # simulating api call
    time.sleep(randint(1, 5))
    print(f"{current_time()}:Middle")


async def intermediate_call():
    # simulating api call
    await asyncio.sleep(randint(1, 5))
    print(f"{current_time()}:Middle")


async def call():
    tasks = []
    for __ in range(10):
        print(f"{current_time()}:Hello")
        tasks.append(asyncio.create_task(intermediate_call()))  # give it to event loop
        print(f"{current_time()}:World")

    await asyncio.gather(*tasks)  # waiting for event loop to close them


def sync_call():
    for __ in range(10):
        print(f"{current_time()}:Hello")
        sync_intermediate_call()
        print(f"{current_time()}:World")


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(call())
    print(f"took:{time.time()-t1} seconds")

    t1 = time.time()
    sync_call()
    print(f"took:{time.time() - t1} seconds")

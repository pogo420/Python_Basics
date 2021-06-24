import asyncio
from asyncio import AbstractEventLoop, Queue
from uuid import uuid4
from datetime import datetime
from random import random
from signal import SIGTERM, SIGINT, SIGHUP


class Message:
    """Class for managing message"""

    def __init__(self, message: str):
        self.__message: str = message
        self.__ack: bool = False
        self.__create_timestamp = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")

    def get_create_timestamp(self) -> str:
        return self.__create_timestamp

    def get_acknowledge_status(self) -> bool:
        return self.__ack

    def acknowledge(self):
        self.__ack = True

    def get_message(self) -> str:
        return self.__message

    def __str__(self):
        return f"""Message{ {"message": self.__message, 
                             "acknowledgment":self.__ack, 
                             "timestamp":self.__create_timestamp} }"""

    def __eq__(self, other):
        if isinstance(other, Message) and (self.__message == other.__message):
            return True
        else:
            return False


async def producer(queue):
    while True:
        message = Message(message=str(uuid4()))
        print(f"Adding message: {message} into queue")
        await asyncio.create_task(queue.put(message))
        await asyncio.sleep(random())  # simulating random IO


async def handle_message(message: Message):
    await save(message)
    await cleanup(message)


async def consumer(queue):
    while True:
        message: Message = await queue.get()
        print(f"Getting data from queue: {message}")
        asyncio.create_task(handle_message(message))
        await asyncio.sleep(random())  # simulating random IO


async def save(message: Message):
    print(f"saving message: {message} to DB")
    await asyncio.sleep(random())  # simulating random IO


async def cleanup(message: Message):
    message.acknowledge()
    print(f"Ack Done message:{message}")
    await asyncio.sleep(random())  # simulating random IO


async def shutdown(signal: int, loop: AbstractEventLoop):
    print(f"Shutting down.., received signal:{signal}")
    # collecting tasks
    tasks = [task for task in asyncio.all_tasks() if task != asyncio.current_task()]
    # cancelling tasks
    [task.cancel() for task in tasks]
    print(f"cancelling {len(tasks)} pending tasks..")
    # waiting for cancel activity to close.
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()


def exception_handler(loop, context: dict):
    print(f"""Error:{context.get("exception")}""")


def main():
    loop: AbstractEventLoop = asyncio.get_event_loop()

    for s in (SIGINT, SIGTERM, SIGHUP):
        loop.add_signal_handler(s,
                                lambda s=s: asyncio.create_task(shutdown(s, loop)))

    # loop.set_exception_handler(exception_handler)
    queue: Queue[Message] = asyncio.Queue()

    try:
        loop.create_task(producer(queue))  # adding tasks to loop
        loop.create_task(consumer(queue))
        loop.run_forever()

    except KeyboardInterrupt:
        print("Process interrupted")

    finally:
        print("Clean up")
        loop.close()


if __name__ == '__main__':
    main()


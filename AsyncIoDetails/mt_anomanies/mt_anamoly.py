
from typing import List, Tuple, Iterator
from requests import Response, get
import concurrent.futures
import time
import sqlite3
from sqlalchemy import create_engine, text


class DBHelper:

    def __init__(self):
        self.__engine = create_engine("sqlite:///mt_anomanies/db/anomany-db.db")
        self.__connection = self.__engine.connect()

    def get_ship_address(self, emp_id) -> Iterator[str]:
        __address_buffer = self.__connection \
            .execution_options(stream_results=True) \
            .execute(text(f"select shipaddress from orders where employeeid={emp_id}")).fetchall()

        for __address in __address_buffer:
            yield __address[0]

    def get_ship_address_batch(self, emp_id) -> Iterator[Tuple[str, ...]]:
        __result = self.__connection\
            .execution_options(stream_results=True)\
            .execute(text(f"select shipaddress from orders where employeeid={emp_id}"))
        while True:
            batch = __result.fetchmany(50)
            batch_rows: Tuple[str, ...]
            if not batch:
                break
            batch_rows = tuple(map(lambda row: row[0], batch))
            yield batch_rows


class ServerHelper:

    def __init__(self):
        self.__base_url: str = "http://127.0.0.1:5000/?user={{user}}"

    def request(self, __address: Iterator[str]) -> str:
        __address_buffer = "-".join(list(__address))
        response1: Response = get(self.__base_url.replace("{{user}}", __address_buffer))
        return response1.text

    def request_batch(self, __address: Iterator[Tuple[str, ...]]) -> str:
        address_batch: Tuple[str, ...]
        response: List[str] = []
        for address_batch in __address:
            __address_buffer = "-".join(list(address_batch))
            response1: Response = get(self.__base_url.replace("{{user}}", __address_buffer))
            response.append(response1.text)
        return "-".join(response)


def process(emp_id: int) -> Tuple[int, str]:
    # no sharing of helper objects.
    addrs = DBHelper().get_ship_address_batch(emp_id)
    response = ServerHelper().request_batch(addrs)
    return emp_id, response


def multi_threads_action(empids: List[int]) -> List[Tuple[int, str]]:
    """Function to implement multi threads"""
    results_: List[Tuple[int, str]]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        temp_ = executor.map(process, empids)
        results_ = list(temp_)
        return results_


def sync_action(empids: List[int]) -> List[Tuple[int, str]]:
    results_: List[Tuple[int, str]] = []
    for emp_id in empids:
        results_.append(process(emp_id))
    return results_


if __name__ == '__main__':
    emp_ids: List[int] = [1, 2, 3, 4, 5, 6, 7]

    # t_init = time.time()
    # results = sync_action(emp_ids)
    # print(f"Results: {results}, it took {time.time() - t_init} seconds via sync approach approach")

    t_init = time.time()
    results = multi_threads_action(emp_ids)
    print(f"Results: {results}, it took {time.time()-t_init} seconds via Multi thread pool approach")

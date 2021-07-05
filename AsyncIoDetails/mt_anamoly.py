from typing import List, Tuple
from requests import Response, get
import concurrent.futures
import time


def task_handler(url: str) -> Tuple[str, str]:
    """Handling synchronous api request"""
    response1: Response = get(url.replace("{{port}}", "5000"))
    response2: Response = get(url.replace("{{port}}", "5001"))
    return response1.text, response2.text


def multi_threads(base_url: str, tasks_: List[str]) -> List[Tuple[str, str]]:
    """Function to implement multi threads"""
    results_: List[Tuple[str, str]]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        url: List[str] = list(map(lambda task: base_url.replace("{{user}}", task), tasks_))
        temp_ = executor.map(task_handler, url)
        results_ = list(temp_)
        return results_


if __name__ == '__main__':
    base_url_: str = "http://127.0.0.1:{{port}}/?user={{user}}"
    tasks: List[str] = ["arnab", "arnablovespython", "ola", "user", "async", "sync", "concurrent", "23iioi32"]

    t_init = time.time()
    results = multi_threads(base_url_, tasks)
    print(f"Results: {results}, it took {time.time()-t_init} seconds via Multi thread pool approach")

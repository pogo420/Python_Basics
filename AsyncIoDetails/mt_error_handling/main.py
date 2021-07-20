from concurrent.futures.thread import ThreadPoolExecutor


class MtException(Exception):
    """Class for exception"""

    def __init__(self, message: str = ""):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__} ({self.message})"


def thread_routine(val: int):
    if val == 3:
        # print(f"Error Value {val} seen")
        raise MtException(f"Value {val} seen")
    else:
        print(f"Good Value {val} seen")


def main():
    with ThreadPoolExecutor() as executor:
        executor.map(thread_routine, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    main()

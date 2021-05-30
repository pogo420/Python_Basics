# reference: https://wiki.python.org/moin/PythonDecoratorLibrary#Cached_Properties
# decorators are design pattern to modify behaviour of a class or function or method
# Decorators exist because you can't just wrap a function or class declaration in a function call.
# A class or function can be a decorator.
# Function as decorator

import time
from functools import wraps


def decorator_function(is_enabled=True):
    def function_wrapper(target_func):
        @wraps(target_func)  # doesn't modify actual function metadata
        def wrapper(*args, **kwargs):  # must return the actual function with args
            if is_enabled:
                start = time.time()
                result = target_func(*args, **kwargs)
                print(f"Function took:{time.time()-start} seconds")
                return result
            return None
        return wrapper  # must return the function object
    return function_wrapper


class _ClassDecorator:
    def __init__(self, function, is_enabled=True):
        self.function = function
        self.is_enabled = is_enabled

    def __call__(self, *args, **kwargs):
        if self.is_enabled:
            start = time.time()
            result = self.function(*args, **kwargs)
            print(f"Function took:{time.time() - start} seconds")
            return result
        return None


def ClassDecorator(function=None, is_enabled=True):
    if function:
        return _ClassDecorator(function)

    def wrapper(function_):
        return _ClassDecorator(function_, is_enabled)

    return wrapper


# @decorator_function()
@ClassDecorator(is_enabled=True)
def random_function(n: int) -> None:
    for i in range(n):
        time.sleep(0.1)
        print(i)


if __name__ == "__main__":
    random_function(7)

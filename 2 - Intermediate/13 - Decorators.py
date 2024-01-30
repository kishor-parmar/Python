import functools
from typing import Any


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do something at start")
        result = func(*args, **kwargs)
        print("Do something at end")
        return result

    return wrapper


@my_decorator
def print_name():
    print("Kish")


# print_name = my_decorator(print_name)

print_name()


@my_decorator
def add5(x):
    return x + 5


result = add5(10)
print(result)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Kish")


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")

    return result


class CountCalls:
    def __init__(self, func) -> None:
        self.func = func
        self.num_calls = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.num_calls += 1
        print(f"This is executes {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()
say_hello()

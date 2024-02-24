from functools import cache, partial, wraps


def with_greeting(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        print("Hello World!")
        return func(*arg, **kwargs)

    return wrapper


@cache
@with_greeting
def add(x, y):
    """Adds two numbers together"""
    import time

    print("running")
    time.sleep(2)

    return x + y


if __name__ == "__main__":
    add(2, 5)
    print(add.__name__)
    print(add.__doc__)

    x = 2
    add2and5 = partial(add, x, 5)
    x = 5
    add2and5()

    add2 = partial(add, 2)
    add2(5)

    print("NOT Cached", add(2, 7))
    print("Cached", add(2, 7))
    print("NOT Cached", add(7, 7))

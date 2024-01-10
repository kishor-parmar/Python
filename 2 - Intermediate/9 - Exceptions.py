# Error and Exceptions


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def main():
    try:
        test_value(4)
        test_value(200)
    except ValueTooHighError as e:
        print(e)
    except ValueTooSmallError as e:
        print(e.message, e.value)


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError("Value is too small", x)


if __name__ == "__main__":
    main()


"""

# x = -5
# if x < 0:
#    raise Exception(f"x should be positive not {x}")

# assert x >= 0, "x is not positive"

try:
    a = 5 / 0
except Exception as e:
    print(e)
else:
    print(" All is fine")
finally:
    print("Cleaing up...")

"""

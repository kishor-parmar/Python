from icecream import ic


def main():
    name = input("What's your name? ")
    ic(hello(name))


def hello(to="world"):
    ic(to)
    return f"Hello, {to}"


if __name__ == "__main__":
    main()

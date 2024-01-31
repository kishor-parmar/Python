# pytest test_hello.py -v
#      or
# cd Tests
# pytest test -v
#

from hello import hello


def test_default():
    assert hello() == "Hello, world"


def test_argument():
    for name in ["Mary", "Mark", "John"]:
        assert hello(name) == f"Hello, {name}"

#
# cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/Respositories
# cd 3\ -\ Testing
#
# pytest tests/test_hello.py -v
#      or
# cd Tests
# pytest test -v
#

import pytest

from source.hello import hello


def test_default():
    assert hello() == "Hello, world"


def test_argument():
    for name in ["Mary", "Mark", "John"]:
        assert hello(name) == f"Hello, {name}"

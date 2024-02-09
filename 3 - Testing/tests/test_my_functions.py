#
# cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/Respositories
# cd 3\ -\ Testing
#
# Tests git:(main) ✗ pytest tests/test_my_functions.py -v
#    or
# cd test
# pytest test_my_functions.py -v
#
# pytest -m slow

import pytest
import time

import source.my_functions as my_functions


def test_add():
    result = my_functions.add(4, 5)
    assert result == 9


def test_add_strings():
    result = my_functions.add("i like ", "burgers")
    assert result == "i like burgers"


def test_divide():
    result = my_functions.divide(50, 5)
    assert result == 10


@pytest.mark.slow
def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(50, 5)
    assert result == 10


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(2, 5) == 7


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(50, 0)

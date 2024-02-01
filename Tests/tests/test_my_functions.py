#
# Tests git:(main) ✗ pytest tests/test_my_functions.py -v
#

import pytest

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


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)

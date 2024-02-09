#
# cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/Respositories
# cd 3\ -\ Testing
#
# Tests git:(main) ✗ pytest tests/test_my_functions.py -v
#


import pytest
import source.shapes as shapes


def test_area(my_rectangle):
    assert my_rectangle.area() == 50


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (5 * 2)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle

# pytest tests/test_square.py -v

import pytest

import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (2, 4), (12, 144)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize(
    "side_length, expected_perimeter", [(3, 12), (4, 16), (10, 40)]
)
def tests_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter

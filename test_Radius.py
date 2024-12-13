import pytest
from Radius import Circle

def test_diameter():
    radius = Circle(7)
    assert radius.diameter() == 14

def test_circumference():
    radius = Circle(2.6)
    assert radius.circumference() == 16.336281798666924

def test_area():
    radius = Circle(10)
    assert radius.area() == 314.1592653589793
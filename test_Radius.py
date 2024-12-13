import pytest
from Radius import Circle

def test_diameter():
    radius = Circle(7)
    assert radius.diameter() == 14

def test_circumference():
    radius = Circle(2.6)
    assert radius.circumference() == 16.3362818
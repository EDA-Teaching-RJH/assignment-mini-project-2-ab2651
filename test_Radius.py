import pytest
from Radius import Circle

def test_diameter():    #This function checks if diameter function correctly operates.
    radius = Circle(7)
    assert radius.diameter() == 14   #The assert keyword checks if the condition in the code is true.

def test_circumference():   #This function checks if the circumference function correctly opertates.
    radius = Circle(2.6)
    assert radius.circumference() == 16.336281798666924

def test_area():   #This function checks if the area function correctly operates.
    radius = Circle(10)
    assert radius.area() == 314.1592653589793
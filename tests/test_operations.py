import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1,1) == 2

def test_subtraction():
    assert subtraction(1,1) == 0

def test_multiplication():
    assert multiplication(1,1) == 1

def test_division_positive():
    assert division(1,1) == 1

def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        division(1,0)
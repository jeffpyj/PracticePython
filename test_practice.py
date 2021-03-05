import pytest
from practice import *

def test_is_multiple():
    assert is_multiple(20,10) == True
    assert is_multiple(20.5, 10.5) == False
    assert is_multiple(200, 0) == "error caught"

def test_is_even():
    assert is_even(100) == True
    assert is_even(15) == False
    assert is_even(99.9) == "error caught"

def test_minmax():
    list_with_floats = [1,5,6.5,-2]
    assert minmax(list_with_floats) == (-2, 6.5)
    list_with_None = [1,None,6]
    assert minmax(list_with_None) == (1, 6)
    list_with_String = [-22,"jeff",None,-22]
    assert minmax(list_with_String) == (-22, -22)

def test_sqr_sum():
    assert sqr_sum(4) == 14
    assert sqr_sum_oneline(4) == 14
    assert sqr_sum(-1) == 0
    assert sqr_sum(4.0) == 0
    assert sqr_sum("hi") == 0
    assert sqr_sum(None) == 0

def test_sqr_odd_sum():
    assert sqr_odd_sum(6) == 35
    assert sqr_odd_sum(-1) == 0
    assert sqr_odd_sum("hello") == 0
    assert sqr_odd_sum(None) == 0
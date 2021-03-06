import pytest
import random
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
    with pytest.raises(TypeError):
        minmax(False)

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

def test_ran_choice():
    int_list = [k for k in range(1,6)]
    func_res = ran_choice(int_list)
    random.seed(103)
    test_res = int_list[random.randrange(0,5)]
    assert func_res == test_res

def test_distince_pair_odd_product():
    assert distinc_pair_odd_product([1,3,4]) == True
    assert distinc_pair_odd_product([1,2,4]) == False
    assert distinc_pair_odd_product([3,3,4]) == False
    assert distinc_pair_odd_product([3,3,5]) == True

def test_all_distinct():
    assert all_distinct([1,3,5,6,7]) == True
    assert all_distinct([1,1,2]) == False
    assert all_distinct([1]) == True
    assert all_distinct([]) == True
    assert all_distinct([1,None,3]) == "error caught"
    with pytest.raises(TypeError):
        all_distinct(1)

def test_dot_product():
    assert dot_product([1,2,3],[3,2,1]) == [3,4,3]
    assert dot_product([1,2,3], [1]) == 0

def test_count_vowel():
    assert count_vowels('a5.3long\\n') == 2
    assert count_vowels('h I  _\t') == 1
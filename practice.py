import collections.abc
from math import sqrt
"""
Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
"""
def is_multiple(n,m):
    try:
        return n/m == n//m
    except ZeroDivisionError:
        return "error caught"

"""Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
"""
def is_even(k):
    try:
        return not (k & 1)
    except TypeError:
        return "error caught"
        

"""Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
"""
def minmax(data):
    if not isinstance(data, collections.abc.Iterable):
        raise TypeError('data must be an iterable type')
    min, max = None, None
    for value in data:
        if type(value) is not int and type(value) is not float:
            continue
        if min == None:
            min, max = value, value
        if (value < min):
            min = value
        if (value > max):
            max = value
    return min, max

"""Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
"""
def sqr_sum(n):
    sum = 0
    if type(n) is not int:
        return sum
    for k in range(1, n):
        sum += k * k
    return sum

def sqr_sum_oneline(n):
    return sum(k * k for k in range(1, n))

"""
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
"""
def sqr_odd_sum(n):
    if type(n) is not int:
        return 0
    return sum(k * k for k in range(1, n) if k & 1)

if __name__ == "__main__":
    gen = [pow(2,k) for k in range(0,9)] 
    print(gen)
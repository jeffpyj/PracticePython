import collections.abc
from math import sqrt
import random
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

"""Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.
"""
def ran_choice(data):
    random.seed(103)
    return data[random.randrange(0,len(data))]

"""Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
"""
def rev_int_list(data):
    j, k = 0, len(data)-1
    while (j < k):
        data[j], data[k] = data[k], data[j]
        j += 1
        k -= 1

"""
Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.
"""
def distinc_pair_odd_product(data):
    #find two distinct odd then product will be odd
    first_odd = 0
    for i in data:
        if i & 1:
            if not (first_odd & 1):
                first_odd = i
            if first_odd != i:
                return True
    return False

"""
Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).
"""
def all_distinct(data):
    if not isinstance(data, collections.abc.Iterable):
        raise TypeError('data must be an iterable type')
    try:
        list.sort(data)
    except TypeError:
        return "error caught"
    if len(data) < 2:
        return True
    i = 0
    for j in range (1, len(data)):
        if data[i] == data[j]:
            return False
        i += 1
    return True

"""
Python's random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns auniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.
"""
def my_shuffle(data):
    random.seed(0)
    upper_bound = len(data)
    for i in range(0, upper_bound):
        swap_i = random.randint(0,upper_bound-1)
        data[i], data[swap_i] = data[swap_i], data[i]

if __name__ == "__main__":
    pow_of_two = [pow(2,k) for k in range(10)] 
    pronic = [n * (n + 1) for n in range (10)]
    a_to_z = [chr(c) for c in range (ord('a'), ord('z') + 1)]
    my_shuffle(a_to_z)
    print(a_to_z)
    

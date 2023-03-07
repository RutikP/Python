"""PYTHON LAMBDA"""

"""LAMBDA FUNCTION"""

# Here lambda used is a keyword after the keyword here two variables are used they are considered arguments follows
# colon and then expression
# raise_to_power = lambda x, y: x ** y

# print(raise_to_power(2, 3))

# =====================================================================================================================

"""MAP AND LAMBDA FUNCTION"""
# Syntax for map() is : map(fun,seq)
# Above syntax defines map has function and sequence as arguments and here seq may be list or others and this map what
# it does is it maps fun to every element in seq(list or others)
# Syntax: map(function,(sqeuence like list,tuple,string and others))
# nums = [2, 4, 6, 8, 10]
# square_all = map(lambda num: num**2, nums)
# print(square_all)
# Printing square_all reveals that its a map object, so to see what it returns, we use list to turn it into a list and
# print the result.
# print(list(square_all))
# --------------------------------------------------
# my_pets = ['alfred', 'tabitha', 'william', 'arla']
#
# uppered_pets = list(map(str.upper, my_pets))
#
# print(uppered_pets)
# --------------------------------------------------
# strings = ["rutik", "ram", "sahil", "krishna"]
# numbers = [1, 2, 3, 4]
# print(list(map(lambda x, y: (x, y), strings, numbers)))
# ----------------------------------------------------
# num1 = [5, 6, 7, 8]
# num2 = [1, 2, 3, 4]
# print(list(map(lambda x, y: (x + y), num1, num2)))
# =====================================================================================================================
"""Example"""
# Define echo_word as a lambda function: echo_word
# echo_word = lambda word1, echo: word1*echo
# Call echo_word and its return value is prints
# print(echo_word('hey', 5))
# =====================================================================================================================
"""Application of lambda function"""
# list_elems = [(2, 4), (122, 3), (1, 331), (19, 0), (126, 8)]
# Sortes by considering every 0th index element from tuple in list by default
# print(sorted(list_elems))
# Sortes by considering every 1th index element from tuple in list by using LAMBDA
# print(sorted(list_elems, key=lambda x: x[1]))

# =====================================================================================================================

# Use that function definition to make a function that always doubles the number you send in:

# def func(n):
    # return lambda a: a*n


# mydoubler = func(2)
# mytripler = func(3)

# print(mydoubler(11))
# print(mytripler(11))

# =====================================================================================================================

# print((lambda x: x * x)(4))

# =====================================================================================================================

"""Use of lambda() with reduce()"""
"""applies a given function to a iterables and returns a single value"""

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)


# =====================================================================================================================

"""Using ZIP"""

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# print(list1+list2)  # It actually concatinate lists
# print(list(zip(list1, list2)))
# it converts like [(1,6),(2,7),(3,8),(4,9),(5,10)]

# =====================================================================================================================

"""Using filter"""
"""filter(), first of all, requires the function to return boolean values (true or false) and then passes each element 
in the iterable through the function, "filtering" away those that are false. It has the following syntax:
filter(func, iterable)
Filter is nthng but it helps to apply conditions on seq"""
# Syntax: filter(fun,seq)
# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# -----------------------------------------------------
# lis = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# print(list(filter(lambda x: x % 3 == 0, lis)))
# ------------------------------------------------------
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# def is_A_student(score):
#     return score > 75
#
# over_75 = list(filter(is_A_student, scores))
#
# print(over_75)
# --------------------------------------------------------
"""printing values which are palindrome from list"""
# palin = ["mohan", "manam", "ramanand", "radar"]
# print(list(filter(lambda words: words == words[::-1], palin)))
# =====================================================================================================================
"""Small Exercise"""
# from functools import reduce
#
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# my_numbers = [4, 6, 9, 23, 5]
#
# map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
# filter_result = list(filter(lambda name: len(name) <= 7, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
# =====================================================================================================================
"""MAP and FILTER together"""

# Example-1
x = map(lambda x: x + x, filter(lambda x: (x >= 4), [1, 2, 3, 4, 5, 6, 7]))
print(list(x))

# Example-2
k = filter(lambda x: (x >= 6), map(lambda x: x+x, [1, 2, 3, 4, 5, 6, 7]))
print(tuple(k))

# =====================================================================================================================
"""MAP and FILTER within REDUCE"""
from functools import reduce
l = reduce(lambda x, y: x+y, map(lambda x: x+x, filter(lambda x: (x>=3), [-1, 0, 1, 2, 3, 4, 5, 6, 7])))
print(l)

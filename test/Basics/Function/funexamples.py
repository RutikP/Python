"""Function Example-1"""


# def fun(name):
#     return f"Hey {name}, Welcome! "
#
#
# def fun2(name):
#     return f"How are you, {name}"
#
#
# def fun3(fun4):
#     return fun4('Rutik')
#
#
# print(fun3(fun))
# print(fun3(fun2))
# ===================================================================================================================
"""Function Example-2"""

# Nested-Function/Inner-Function

# ----------------------------------------------
# def fun():
#     print("This is first Function")
#
#
#     def func1():
#         print("This is Inner-function/child function")
#
#
#     def func2():
#         print("This is second Inner-function/child function")
#     func1()
#     func2()
#

# def plus_one(num):
#     def add_one(num):
#         return num+1
#
#     result = add_one(num)
#     return result
#
#
# print(plus_one(9))
#
# fun()
# --------------------------------------
# ======================================================================================================================
"""Function Example-3"""

# Function as a Arguments



# def fun(n):
#     def fun1():
#         return "Returns func1"
#
#
#     def fun2():
#         return "Returns func2"
#     if n == 1:
#         return fun1
#     else:
#         return fun2
#
#
# a = fun(1)
# b = fun(2)
# print(a())
# print(b())

# ======================================================================================================================
"""Function Example-4"""
# Passing Functions as Arguments to other Functions


# def plus_one(num):
#     return num+1
#
#
# def function_call(function):
#     add_with_num = 8
#     return function(add_with_num)
#
#
# print(function_call(plus_one))

# ======================================================================================================================

"""Function Example-5"""
# Functions Returning other Functions


# def hello_function():
#     def say_hello():
#         return "Hi"
#     return say_hello()
#
#
# hello = hello_function()
# print(hello)



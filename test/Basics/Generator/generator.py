# """Fibonacci Series Using Generator"""
# a = 0
# b = 1
#
#
# def gen(h):
#     c = 0
#     while i < h:
#         global a
#         global b
#         c = a + b
#         a = b
#         b = c
#         yield c
#
# res = 0
# n = int(input("Enter num: "))
# if n>=1:
#     print(a, end=" ")
# if n>=2:
#     print(b, end=" ")
#     res = gen(n-2)
#
#
# for i in range(n-2):
#     print(next(res), end=" ") # You can use res.__next__() also.


import random

mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2))
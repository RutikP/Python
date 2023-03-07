# class Dog:
#     def __init__(self):  # This is the initializer that you can later use to
#         pass                   # instantiate objects. It's similar to a constructor in Java.

# self in Python is equivalent to this in C++ or Java.

# Instantiating objects
"""To instantiate an object, type the class name, followed by two brackets. 
You can assign this to a variable to keep track of the object."""

# tommy = Dog()

# print(tommy)

# ===============================================================================================

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print("bark! bark!")
#     def Doginfo(self, village):
#         self.village = village
#         print(f"{self.name} is {self.age} old and lives in {self.village}")





# dog1 = Dog("Rocky","2 years")
#
# print(dog1.name)
# print(dog1.age)
#
# print(f"{dog1.name} is {dog1.age} old")
# about_dog1 = f"{dog1.name} is {dog1.age} old"
# print(about_dog1)
#
# dog1.bark()
# dog1.Doginfo("Kerala")
#
# fifu = Dog("Fifu", "3 years")
# fanny = Dog("Fanny", "30 Days")
# kiku = Dog("Kiku", "20 Days")
#
# fifu.Doginfo("Bidar")
# kiku.Doginfo("Gulbarga")
#
# fifu.age = "1 year"
#
# fifu.Doginfo("Bangalore")

# =============================================================================================

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     'This is just a Docs'
#
#
#
# person1 = Person("Rutik", "20 years")
# print(person1.age)

# ================================================================================================
"""Deleting Attributes and Objects"""

# class ComplexNum:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#
#     def getdata(self):
#         print(f'{self.real}+{self.img}j')
#
#
# num1 = ComplexNum(5,6)
# num2 = ComplexNum(2,8)
# #
# num1.getdata()
# num2.getdata()

# Deleting the attribute/method of class
# del ComplexNum.getdata
# num1.getdata()
# AttributeError: 'ComplexNum' object has no attribute 'getdata'

# del num1

# num1.getdata()
# after deleting object if we call method using that object we get
# NameError: name 'num1' is not defined
# =======================================================================================================

"""Destructor in Python OOP"""
# Ex-1

# Python program to illustrate destructor
# class Employee:

    # Initializing
    # def __init__(self,name):
    #     self.name = name
    #     print('Employee created.')

        # Deleting (Calling destructor)

    # def __del__(self):
    #     print('Destructor called, Employee deleted.')


# obj = Employee("Rutik")
# del obj
# print(obj.name)

# Ex-2

# class Employee:

    # Initializing
    # def __init__(self, name):
    #     self.name = name
    #     print('Employee created')

        # Calling destructor

    # def __del__(self):
    #     print("Destructor called")


# def Create_obj():
#     print('Making Object...')
#     obj = Employee("Rutik")
#     print('function end...')
#     return obj


# print('Calling Create_obj() function...')
# obj = Create_obj()
# print('Program End...')
#
# print(obj.name)

# Here, notice that the destructor is called after the ‘Program End…’ printed.

# =====================================================================================================

# marks = ["FA1", 80, "FA2", 85, "FA3", 95]
# report = marks[-4:]
# report = report[:1]+marks[5:]
# print(report)

# list1 = [10, 20, 0, 40, 0]
# def test():
#     try:
#         i=3
#         if(list1[i]/list1[i+1]>1):
#             value  = i + 1
#     except ZeroDivisionError:
#         print("1")
#     except IndexError:
#         print("2")
#     finally:
#         print("4")
#     print("5")
# test()

# for i in range(1,6):
#     for j in range(1,6):
#         if(i%j != 0):
#             pass
#         elif(j<i):
#             continue
#         else:
#             print(i*j)


# num1 = 11//10
# num2 = 11%10
# num3 = 20
# num4 = 40
# num5 = 5
#
# if(num3>num4):
#     if(num3>num5):
#         print(num5*num4/num3)
#     else:
#         print(num3/num5)
# else:
#     if(num1 == num2):
#         print(num4/num3)
#     else:
#         print(num4/num5)


# i = 0
# j = 10
# while i<=10 and j>=1:
#     print(i, j)
#     j = j-1
#     i = i+1
#     if(i == j):
#         break

# temp = "Hello? how are you?"
# if(temp.isdigit()):
#     temp += "fine"
# else:
#     for i in range(len(temp)):
#         if(temp[i] == '?'):
#             final_val = temp[:i]
#             break
# if(final_val.endswith('u')):
#     final_val.replace('you', 'u')
# else:
#     final_val = final_val.upper()
# print(final_val)

# code = "jack and jill went up the hill"
#
# for temp in code.split():
#     if(temp.endswith("ill")):
#         print("Count: ", code.count("ill"))
#         break
# code = code.replace("j", "m")
#
# for temp in code.split():
#     if(len(temp)%2 != 0):
#         k = (str)(temp)
#         code = code.replace(k, k.upper())
#     print(code)


# def fun(n):
#     if n < 1:
#         return 0
#     elif n%2 == 0:
#         return fun(n-1)
#     else:
#         return n + fun(n-2)
#
# val = fun(11)
# print(val)

# def calculate(x, y):
#     while(x != y):
#         if(x > y):
#             return calculate(x-y, y)
#         else:
#             return calculate(x, y-x)
#     return x
#
# m = calculate(45, 20)
#
# print(m)


# a = 5
# b = 5
# c = 1
# d = 1
# i = 0
# # t = (a+b) > (c/d) and i <= (a-c*b)
# m = not ((d>=b) or (a==c))
# # print(t)
# print(m)


# def fun(a, b):
#     try:
#         c = (int)(a)
#         b = c+"A"
#         print(b)
#     except TypeError:
#         print("T")
#     finally:
#         print("IF")
# try:
#     fun('R', 13)
# except ValueError:
#     print("V")
# finally:
#     print("OF")

# list1 = [1, 2, 1, 3, 3, 1, 2, 1, 2, 1]
# tuple1 = ("A", "B", "C", "D")
# tuple1 += ("E", )
# list2 = []
# for i in range(5, len(list1)):
#     list2.append(list1[i-5]+list1[i])
# for i in range(0, len(list2)):
#     print(tuple1[i], list2[i])

# def func(sample, res, key, val):
#     if(key in sample):
#         res = True
#         sample.update({key:val})
#     res = False
# res = None
# sample = {"XS":1, "X":0, "XL":3, "XXL":4}
# func(sample, res,"X", 2)
# print(sample["X"], res)\


# my_str = "All3 that4 glitters8 is2 not3 gold4"
# my_lst=[]
#
# for char in my_str:
#     if(char.isdigit()):
#         my_lst.append((int)(char))
#         my_str = my_str.replace(char," ")
# print(my_str, my_lst)



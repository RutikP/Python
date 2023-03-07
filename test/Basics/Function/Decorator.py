"""Example-1"""
# def upper_case_decorator(function):  # Here argument function is "say_hi()"
#     def wrapper():
#         func = function() #  Here function() is actually say_hi which is passed as argument to "upper_case_decorator"
                             #  so say_hi returns "Hello there" and stored in func
#         make_uppercase = func.upper() #  Here "Hello there" is converted to upper case
#         return make_uppercase
#     return wrapper
#
#
# def say_hi():
#     return "Hello there"


# decorate = upper_case_decorator(say_hi) #  Always remember while passing function as argument to function,
# print(decorate())                        #  don't append () to function while using it in functions argument

# -------------------------------------------------------------------------------------------------------------------
"""Example-1"""
def multiplication(function):
    def wrapper():
        func = function()
        func1 = func*9
        return func1
    return wrapper


def number():
    return 8


decorate = multiplication(number)
print(decorate())
# -------------------------------------------------------------------------------------------------------------------
"""Example-3"""


# def multiplication(function):
#     def wrapper():
#         func = function()
#         func1 = func+" there"
#         return func1
#     return wrapper
#
#
# @multiplication #  It is called pysyntax/syntatic sugar
# def number():
#     return "Hi"
#
#
# print(number())

# -------------------------------------------------------------------------------------------------------------------


"""Example-4"""


# def multiplication(function):
#     def wrapper():
#         function()
#         print("I am Rutik")
#     return wrapper
#
#
# @multiplication #  It is called pysyntax/syntatic sugar
# def number():
#     print("Hi there")
#
#
#
# number()


# -------------------------------------------------------------------------------------------------------------------


"""Example-5"""


# def name(function):
#     def wrapper():
#         func = function()
#         if func.isdigit():
#             print("It is integer")
#         else:
#             print("It is string")
#     return wrapper
#
#
# @name #  It is called pysyntax/syntatic sugar
# def anything():
#     something = input("Type anything either int or str: ")
#     return something
#
#
# anything()

# =====================================================================================================================
"""Example-6"""


# def name(function):
#     def wrapper():
#         func = function()
#         if func.isdigit():
#             return "It is integer"
#         else:
#             return "It is string"
#     return wrapper
#
#
#
# def anything():
#     something = input("Type anything either int or str: ")
#     return something
#
#
# returning = name(anything)
# print(returning())

# =====================================================================================================================
"""Accepting Arguments in Decorator Functions"""
"""Example-1"""
# def Decorator_with_arguments(function):
#     def wrapper_accepting_arguments(args1, args2):
#         print("My arguments are: {0}, {1}".format(args1, args2))
#         function(args1, args2)
#     return wrapper_accepting_arguments
#
#
# @Decorator_with_arguments
# def simple(city_1, city_2):
#     print("The city i loved are: {0} and {1}".format(city_1, city_2))
#
#
# simple("Bangalore", "Mangalore")
"""Example-2"""
# def Decorator_with_arguments(function):
#     def wrapper_accepting_arguments(args1, args2):
#         print("My arguments are: {0}, {1}".format(args1, args2))
#         function(args1, args2)
#     return wrapper_accepting_arguments
#
#
# @Decorator_with_arguments
# def simple(city_1, city_2):
#     print(f"The city i loved are: {city_1} and {city_2}")  # Here String interpolation is used
#
#
# simple("Bangalore", "Mangalore")

# =====================================================================================================================
"""Defining General Purpose Decorators"""
"""Example-1"""

def function_with_arguments(function):
    def wrapper_accepting_arguments(*args, **kwargs):
        print("args values are: ", args)
        print("Positioning arguments are: ", args)
        print("The keyword arguments are: ", kwargs)
        function(*args)
    return wrapper_accepting_arguments


# @function_with_arguments
"""The below two lines of code is a decorator function used for passing positioning arguments"""
# def arguments_inserting_fun(a, b, c):
#     print(a, b, c)

""" the below code is used to call arguments_inserting_fun() with passing arguments as positioning arguments"""
# arguments_inserting_fun("Apple", "Banana", "Mango")

"""the below two lines of code is a decorator used for passing keywords arguments"""
# def arguments_inserting_fun():
#     print("This has shown keyword arguments")

"""the below code is used to call arguments_inserting_fun() with passing arguments as keywords"""
# arguments_inserting_fun(fruit1="Apple", fruit2="Banana", fruit3="Mango")


# =====================================================================================================================

"""Defining General Purpose Decorators"""
"""Example-2"""


# def function_accepts_arguments(function):
#     def wrapper_accepts_Arguments(*args, **kwargs):
#         print("The positioning arguments are: ", args)
#         print("The keyword arguments are: ", kwargs)
#         function(*args)
#     return wrapper_accepts_Arguments
#
#
# @function_accepts_arguments
# def argument_passing_fun():  # when argument as keywords in function definition nthng is passed as arguments
#     print("This shown as the keyword arguments")
#
#
# argument_passing_fun(animal1="Tiger", animal2="Lion")

# =====================================================================================================================







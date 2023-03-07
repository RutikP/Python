# List is a collection which is ordered and changeable.Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable.Allows duplicate members.
# Set is a collection which is unordered and unindexed.No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed.No duplicate members.


# subjects = ['physics', 'Chemistry', 'Maths', 'Biology', 'physics']
# print(subjects)
# # Reverse of subjects list
# print(subjects[::-1]) Which is used to reverse the list
# print(subjects[2])
# subjects[2] = 'Botany'
# print(subjects)
# print(subjects[0:4]) # Which gives index from 0->3
# print(len(subjects))
# print(subjects*2)
# # ----------------------------------------------------------------------------------------------------------------------
# Python list remove duplicates
# A = list(dict.fromkeys(subjects))
# print(A)
# # ----------------------------------------------------------------------------------------------------------------------
# # Sorting of list
# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print(cars)
# numbers = [1, 2, 8, 6, 4, 5, 3, 7]
# numbers.sort()
# print(numbers)
# # ---------------------------------------------------------------------------------------------------------------------
# spam = [['cat', 'bat'],[10, 20, 30, 40, 50]]
# print(spam[0][1])
# print("my "+spam[0][0]+" is very cute")
# print(spam[0:1])
# print(spam[:1])
# print(spam[0:])
# print(len(spam))
# spam[1]=spam[0]
# print(spam)
# # ----------------------------------------------------------------------------------------------------------------------
# odd = [1, 3, 5]
# even = [2, 4, 6]
# odd = odd + even
# print(odd)
# # ----------------------------------------------------------------------------------------------------------------------
# # deleting an element from list
# odd = [7, 9, 11]
# del odd[1]
# print(odd)
# # The "in" and "not in" operators
# print(7 in odd)
# print(9 not in odd)
# # ----------------------------------------------------------------------------------------------------------------------
#
#
# # The Multiple assignment trick
# cat = ['fat', 'black', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
# print(cat)
#
# # Augmented assignment operators
# spam = 43
# spam += 1
# print(spam)
#
# spam = 'Hello'
# spam += ' world'
# print(spam)
#
# spam = ['a', 'z', 'A', 'Z']
# spam.sort(key=str.lower)
# print(spam)
# # ---------------------------------------------------------------------------------------------------------------------
# #Mutable and Immutable Data Types
# #Immutable
# name = 'Rutik a superman'
# name[7]='the'
# print(name)
#
# # Mutable
# name = 'Rutik a Superman'
# newname = name[0:6]+'the'+name[7:16]
# print(newname)
# # ----------------------------------------------------------------------------------------------------------------------
# # Converting Types with the list() and tuple() Functions
# print(tuple(['cat', 'dog', 42]))
# print(list(('cat', 'dog', 42)))
# print(type(tuple(['cat', 'dog', 42])))
# print(type(list(('cat', 'dog', 42))))
# # ----------------------------------------------------------------------------------------------------------------------
# # References
# spam = 42
# cheese = spam
# spam = 43
# print(cheese)
# print(spam)
# #-----------------------------------------------------------------------------------------------------------------------
# spam = [1,2,3,4,5]
# cheese = spam
# print(spam)
# cheese[0] = 'Hello'
# print(cheese)
# print(spam)
# #-----------------------------------------------------------------------------------------------------------------------
# # good examples
# mine = ['pen', 'book', 'laptop']
# print("Enter a name")
# name = input()
# if name not in mine:
#     print(name+' is not mine')
# else:
#     print(name+' is mine')
#
#
#
# print()
#
# #----------------------------------------------------------------------------------------------------------------------
# def swap(alpha):
#     size = len(alpha)
#     temp1 = alpha[0]
#     alpha[0] = alpha[size - 1]
#     alpha[size - 1] = temp1
#     return alpha
#
#
# alpha = ['a', 'b', 'c', 'd']
# print(len(alpha))
# print(alpha.count('a'))
#
# print(swap(alpha))
#
#
#
#
# print()
# # ----------------------------------------------------------------------------------------------------------------------
# elements = ['a', 1, 'b', 4, 't', 'ya', 89
#
#
# def search(ele):
#     size = len(elements)
#     i = 0
#     while i < size:
#         if ele == elements[i]:
#             print(ele, " is present ", i, " index")
#             break
#         else:
#             i = i+1
#
#
# print(search('a'))
#
# print()
# print()
# print()
#
# # ----------------------------------------------------------------------------------------------------------------------
# newindia = [['mumbai', 48374], ['karnataka', 23783], ['delhi', 32352],
#             ['bangalore', 24534], ['bhalki', 23435], ['bihar', 35322],
#             ['goa', 42352], ['kerala', 35223], ['gulbarga', 23532]]
#
# # METHODS of FUNCTIONS TO PRINT NEWINDIA


# def report1(state_data):
#     print("population       state")
#     for state_item in state_data:
#         print(state_item[1], "          ", state_item[0])
#
#
# print(report1(newindia))
#
# print()
# print()
# print()


# def report2(state_data):
#     print("population        state")
#     for i in range(0, len(state_data)):
#         print(state_data[i][1], "          ", state_data[i][0])
#
#
# print(report2(newIndia))
#
# print()
# print()
#
#
# newIndia = [['mumbai', 48374], ['karnataka', 23783], ['delhi', 32352],
#             ['bangalore', 24534], ['bhalki', 23435], ['bihar', 35322],
#             ['goa', 42352], ['kerala', 35223], ['gulbarga', 23532]]


#
#
#
#
#


# def report2(state_data):
#     k = 0
#     num_data = len(state_data)
#     print("population        state")
#     for i in range(0, num_data):
#         print(state_data[i][1], "          ", state_data[i][0])
#
#     for j in range(0, num_data):
#         one = state_data[j]
#         pop = one[1]
#         k = k + pop
#     print("Total sum is ", k)
#     avg = k / (len(state_data))
#     print("Average population is ", avg)
#
#
# print(report2(newindia))



# import random


# Inserting Random Number in list
# Num = []
# appendNum = int(input("How many random numbers you want in list"))
# n = int(input("Enter the each random num's range"))
# no = 0
# while no < appendNum:
#     addNum = Num.append(int(n * random.random()) + 1)
#     no = no + 1
# print(Num)

# =================================================================================================================
import sys
lis = []
num = 0


def cal(x):
    j = 0
    for i in x:
        i += j
    res = int(j//len(x))
    print("Avg: ", res)


def avg():
    global num
    global lis
    num = input("Enter number")
    if num.isdigit():
        num = int(num)
        lis.append(num)
        avg()
    elif num == "end":
        cal(lis)
        sys.exit()
    else:
        sys.exit()



avg()

# =======================================================================================================

lis = [1, 2, 3]
lis1 = [4, 5, 6]
lis2 = lis + lis1
print(lis2)










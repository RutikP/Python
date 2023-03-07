# name = ''
# while name != 'your name':
#     print("Please type your name.")
#     name = input()
# print("Thank You!!")

# print(0o11)  # octal number 77 in decimal is 9

# print(0x24)  # Hexadecimal number 24 in decimal is 36

# i = 1
# while i<5:
#     print(i)
#     i +=1
#     if i == 3:
#         break
# else:
#     print("While completed successfully")

# print(oct(16))
# print(hex(36))
# -----------------------------------------------------------------------------------------------------------------------


# import array

# a = array.array('i', [1, 3, 5])
# b = array.array('i', [2, 4, 6])
# c = array.array('i')
# c = a + b
# print(a)
# print(c)
# c.reverse()
# print(c)
# m = array.array('q', [9, 8, 6, 12, 51])
# a.append(9)
# a.insert(3, 20)
# a.extend([12, 23, 43])
# a.pop(2)
# print(a)

# m.remove(6)  # remove function is used when you know what element you want to delete but you don't know the index then
# directly use that element in remove function to delete

# print(m)


# ======================================================================================================================


# clgs = ['Acharya', 'Reva', 'RV', 'BIT', 'MS Ramaihah', 'PES', 'RV', 'Reva']
# print(clgs[1:])
# print(clgs[::-1])
# print(clgs[::5])
# a = list(dict.fromkeys(clgs))
# print(a)
# del clgs[0]
# print(clgs)
# if 'BU' not in clgs:
#     print("True")
# else:
#     print("False")



# type conversion
# here list is converted to tuple
# A = tuple(['a', 4, 'ay'])
# print(A)
# here tuple is converted to list
# B = list((4, 'ad', 'ay', 14))
# print(B)




# i = 0
# elems = []
# n = int(input("Enter the no. of elements"))
# print("Enter elements")
# while i < n:
#     ele = int(input())
#     elems[i] = ele
#     i = i + 1
# print(elems)
# # sort()

# ============================================================================================================
# Using Dictionary

# sub = {51: "M & E", 52: "CN", 53: "DBMS", 54: "ATC", 55: "ADP", 56: "UNIX"}
# Printing items

# print(sub)

# Accessing Items

# print(sub[51])
# print(sub.get(53))

# Keys and Values
# print(sub.keys(), sub.values())

# Changing/Updating values
# sub[53] = "DS"
# print(sub)

# Printing only keys

# for x in sub:
#     print(x, end=" ")
# print()
# OR
# for x in sub.keys():
#     print(x, end=" ")
# print()

# Printing only values

# for x in sub:
#     print(sub[x], end=", ")
# OR
# for x in sub.values():
#     print(x, end=" ")


# Using "in" and "not in"
# k = 52 in sub
# print(k)
#
# r = 57 in sub
# print(r)

# Dictionary will not allow the duplicate values to print:

# courses = {1: "JAVA", 2: "PYTHON", 3: "IOT", 4: "JS", 5: "ANGULAR", 6: "ASP.NET", 4: 104}
# print(courses)

# Some Methods:

# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# zoo = {1: "lion", 2: "Tiger", 3: "Monkey", 4: "Deer", 5: "Peacock"}
# x = zoo.items()
# x = zoo.keys()
# x = zoo.pop(2)  # Here we have to specify item key to delete that key value
# print(x)
# print(zoo)
# l = zoo.popitem()  # Here no need to specify item key automatically it will delete the last item
# print(zoo)
# del zoo[1]
# print(zoo)
# m = zoo.setdefault(3, "Rabbit")
# print(zoo)
# update = zoo.update({3: "Rabbit"})
# print(zoo)
# newzoo = zoo.copy()
# print(newzoo)

# thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
# print(thisdict)








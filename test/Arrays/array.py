# import array
#
# a = array.array('i', [1, 2, 3, 45, 6])  # here "i" is an index
# print(a)
#
# print(a[2])
# print(a[-1])
# print(a[4])
#
# # Finding the length of the array
# print(len(a))
# # ----------------------------------------------------------------------------------------------------------------------
# # Some operations on array
# a.append(3)
# print("After appending 3 we get an array is =", a)
# a.extend([4, 35, 31])
# print("After extending some values to array a we get an array is =", a)
# a.insert(4, 20)
# print(a)
# print("removing last element using pop i.e.,", a.pop())
# print(a)
# print("removing 4th element using pop i.e.,", a.pop(3))
# print(a)
# print("Element 2 is removed")
# a.remove(2)
# print(a)
# # ----------------------------------------------------------------------------------------------------------------------
# # Array concatenation
# a = array.array('d', [2.3, 4.3, 42.2])
# print("Array a =", a)
# b = array.array('d', [5.3, 32.3, 75.3])
# print("Array b =", b)
# c = array.array('d')
# c = a + b
# print("After concatenating a and b we get: Array c =", c)
# # ----------------------------------------------------------------------------------------------------------------------
# # Slicing an Array
# A = array.array('l', [1, 3, 4, 3, 55, 2])
# print("Array A =", A)
# print("Reverse of array A: ", A[::-1])
# d = A[0:3]
# print("After Slicing")
# print("A =", d)
# print()
# # ----------------------------------------------------------------------------------------------------------------------
# # Loops using Arrays
# print("                            Loops Using arrays                                                             ")
# print("                            ------------------                                                              ")
#
# print(A)
# for x in A:
#     print(x, end=" ")
# print()
# # Slicing and printing the specific elements
#
# for y in A[2:5]:
#     print(y, end=" ")
# print()
# F = array.array('d', [1, 2, 3, 4, 5, 6, 7, 8])
# temp = 0
# temp = int(temp)
# while temp < F[4]:
#     print(F[temp], end=" ")
#     temp = temp + 1
#
# import array
# m = array.array('i', [2, 4, 6, 8, 12, 16, 20])
# print(m)
# for z in m:
#     print(z, end=" ")
#
# # # ----------------------------------------------------------------------------------------------------------------------
# import array as arr
#
# # array with int type
# a = arr.array('i', [1, 2, 3])
#
# print("Array before insertion : ", end=" ")
# for k in range(0, 3):
#     print(a[k], end=" ")
# print()
# # ----------------------------------------------------------------------------------------------------------------------
#
#


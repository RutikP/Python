# here on SET duplicate values are not counted here
myset = {10, 20, 30, 10, 40, 'rahul', 40, 'sahil'}
print(myset)
# print(myset[3])  so here it gives error because SET will not be having indexing it gives random values.
# some set operations.

A = {1, 3, 5, 7, 9}
B = {2, 4, 6, 8, 10, 1}
print(A | B)  # Union
print(A & B)  # Intersection
print(A - B)  # Difference
B.remove(8)  # REMOVE which delete specified element in the list
print(B)
A.add(6)
print(A)
A.pop()  # POP removes first element in the list unlike REMOVE(Which removes specified element)
print(A)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)





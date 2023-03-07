



def BSearch(elements, low, high, x):
    if (x <= elements[int(high)]) and (x >= elements[int(low)]):
        mid = (low + high) / 2
        if x == elements[int(mid)]:
            return mid
        elif x < elements[int(mid)]:
            return BSearch(elements, 0, mid - 1, x)
        else:
            return BSearch(elements, mid + 1, len(elements) - 1, x)
    else:
        return -1






arr = []
print("Enter list size: ")
n = int(input())
print("Enter list of elements")
size = int("0")
while size < n:
    ele = int(input())
    arr.append(ele)
    size = size + 1

arr.sort()

elements = []


for i in range(len(arr)):
    elements.append(arr[i])
print("Sorted array elements are: ")
for i in range(len(elements)):
    print(elements[i], end=" ")

keyele = int(input("\nEnter key element to search"))

low = 0
high = len(elements) - 1


result = int(BSearch(elements, low, high, keyele)+1)
"""if you entered num in range b/w elements[low]-elements[high] if
 that element is not found in array then from BSearch fun it returns -1 and result becomes 0 and we get "element not found" 
 msg; And if you entered searchele num which is not in range of elements[low]-elements[high] from fun BSearch
  else part will be executed and returns -1 and we get result as 0 so we get msg "element not found" msg """
if result != 0:
    print("Element found at position "+str(result))
else:
    print("Element not found")














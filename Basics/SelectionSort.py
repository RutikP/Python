


def sort():
    # temp = int("0")
    j = 0
    min_index = j

    for j in range(0, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[min_index] > arr[k]:
                min_index = k
        # arr[j], arr[min_index] = arr[min_index], arr[j]
        temp = arr[min_index]
        arr[min_index] = arr[j]
        arr[j] = temp


    for m in range(len(arr)):
        print(arr[m], end=" ")




arr = []
n = int(input("Enter the no. of elements"))
print("Enter elements")
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
    i = i + 1
sort()



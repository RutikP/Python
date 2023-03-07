def res(arr,n):
    for i in range(1,n+1):
        if i % 2 == 0:
            continue
        else:
            print(arr[i-1],end=" ")

print("elements: "+"\n")
n = int(input())
arr = list(map(int, input().split()))

res(arr,n)
    

    
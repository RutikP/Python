import math
def check(n,maxm):
    for i in range(n, maxm+1):
        for j in range(2,maxm):
            if i%j == 0:
                break
            else:
                print(str(i)+" ",end=" ")
                break
                
                
    
print("Enter number")
n = int(input())
maxm = int(input())
check(n,maxm)

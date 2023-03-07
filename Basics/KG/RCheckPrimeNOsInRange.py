import math
def check(n):
    for i in range(2,n+1):
        if n%i == 0:
            if i == n: 
                print(str(i)+" is a prime number ")
                break
            else:
                break
                
                
    
print("Enter number")
n = int(input())
maxm = int(input())
for i in range(2,maxm+1):
    check(i)

import math
def check(n):
    for i in range(1,n+1):
        if n%i == 0:
            if i == 1:
                continue
            if i == n:
                sr = math.sqrt(n)
                print("Number is a prime number "+str(sr))
            else:
                print("Number is not a prime ")
                break
                
                
    
print("Enter number")
n = int(input())
check(n)

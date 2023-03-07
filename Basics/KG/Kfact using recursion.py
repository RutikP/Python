
def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)
    
    
    
print("Enter Number")
num = int(input())
print(fac(num))
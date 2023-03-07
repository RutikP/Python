
def fac(n):
    res = 1
    for i in range(1,n+1):
        res = res*i 
    return res
        
    
    
print("Enter Number")
num = int(input())
print(fac(num))
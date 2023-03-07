import math
lis=[]
def check(n):
    for i in range(2,n+1):
        if n%i == 0:
            if i == n: 
                print(str(i)+" is a prime number ")
                lis.append(i)
                break
            else:
                break      
                
    
print("Enter Range")
n = int(input())
maxm = int(input())
for i in range(2,maxm+1):
    check(i) 
summ=int(0)
for i in lis:
    summ = summ + i
print("Summation of prime numbers are: "+str(summ))

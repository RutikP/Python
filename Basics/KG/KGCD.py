
def GCD(n1,n2):
    n = max(n1,n2)
    lis = []
    for i in range(1,n1+1):
        if n1%i == 0 and n2%i==0:
            lis.append(i)
    print(max(lis))
    
print("Enter two numbers")
n = input().split()

n1 = int(n[0])
n2 = int(n[1])
GCD(n1,n2)
    
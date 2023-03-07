def GCD(n1,n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 == n2:
        return n1
    if n1 > n2:
        return GCD(n1-n2,n2)
    return GCD(n1,n2-n1)

print("Enter two numbers")
n1 = int(input())
n2 = int(input())
print(GCD(n1,n2))
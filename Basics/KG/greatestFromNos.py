def greatest(n1,n2,n3):
    if n1>n2 and n1>n3 and n1!=n2!=n3:
        print(str(n1))
    if n2>n1 and n2>n3 and n1!=n2!=n3:
        print(str(n2))
    if n3>n2 and n3>n1 and n1!=n2!=n3:
        print(str(n3))
    
    
print("Enter three numbers")
n = input().split()
n1 = int(n[0])
n2 = int(n[1])
n3 =int(n[2])
greatest(n1,n2,n3)
    


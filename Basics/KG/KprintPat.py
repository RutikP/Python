def printPat(N):
    a = N
    while a>0:
        b=N
        while b>0:
            c=a
            while c>0:
                print(b,end=" ")
                c = c - 1
            b = b - 1 
        a = a - 1
        print()
    
n = int(input())
printPat(n)
    
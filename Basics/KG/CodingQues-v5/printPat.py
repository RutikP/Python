def printPat(N,K):
    count = 0
    if N>0:
        for i in range(1,K+1):
            for j in range(1,N+1):
                print(i,end=" ")
            if i==K:
                print("\n")
                N = N -1 
                printPat(N,K)
        
n = int(input())
k = n
printPat(n,k)
    
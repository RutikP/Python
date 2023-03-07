ntterm = int(input("Upto how many terms?"))

n1 = 0
n2 = 1
count = 0
if ntterm <= 0:
    print("Enter +ve term")
elif ntterm == 1:
    print("Fibonacci sequence upto", ntterm, "is", end=" ")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < ntterm:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1








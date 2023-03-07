n = input("Enter the number")
n = int(n)

for i in range(n, 0, -1):
    for j in range(i - 1, 1, -1):
        if i % j == 0:
            print(i, " is divisible by", j)
        else:
            print(i, " is not divisible by ", j)

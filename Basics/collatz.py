import sys


try:
    num = int(input("Enter the number"))
except ValueError:
    print("Enter number not string")


print(num)
res = 0


def collatz(x):
    if(x % 2) == 0:
        return int(x//2)
    else:
        return int(3*x+1)


def loop():
    global res
    global num
    res = collatz(num)
    if res == 1:
        print("1")
        sys.exit()
    else:
        print(res)
        num = res
        loop()


loop()





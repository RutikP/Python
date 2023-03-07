import sys

lis = []
num = 0


def cal(x):
    j = 0
    res = 0
    res = float(res)
    for i in x:
        j += i
    y = len(x)
    res = float(j/y)
    print("Avg: ", res)


def avg():
    global num
    global lis
    x = "end"
    num = input("Enter number: ")
    if num != x:
        if num.isdigit():
            num = int(num)
            lis.append(num)
            avg()
        else:
            print("Enter num to add in list or enter \"end\" to get avg")
            avg()

    elif num == "end":
        if len(lis) != 0:
            cal(lis)
            sys.exit()
        else:
            sys.exit()



avg()
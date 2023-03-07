import sys


lis = []


def lisvalues(x):
    print()
    print(x)
    print()
    m = len(x)-1
    n = 1
    for i in x:
        if n <= m:
            print(i, end=", ")
            n = n + 1
        else:
            print("and ", i)



def createlis():
    k = "end"
    ele = input("Enter the elems ")
    if ele == k:
        lisvalues(lis)
        sys.exit()
    else:
        lis.append(ele)
        createlis()


createlis()
import math
def AOC(n):
    n = float(n/2)
    res = 3.14*n*n
    #nres = round(res,2)
    return res
print("Enter diameter of circle ")
ip = float(input())
res = AOC(ip)
print("%.2f" % res)
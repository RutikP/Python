def printfile(filename):
    infile = open(filename)
    for line in infile:
        print(line, end="")


printfile("ADream.txt")



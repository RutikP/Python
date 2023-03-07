import sys

print("Name of the script is: ",sys.argv[0])
print("The value of the argument is: ",sys.argv[1])
print("The length of the arguments is:",len(sys.argv))

c = int(sys.argv[1]) + int(sys.argv[2])
print(c)

print("Argument List:",str(sys.argv))

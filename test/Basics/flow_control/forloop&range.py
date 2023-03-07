print("What is ur name")
for i in range(5):
    print('Rutik (' + str(i) + ')')
print()
#  sum of first 6 numbers
total = 0
for val in range(6):
    total = total + val
print(total)
print()

for i in range(0, 35, 7):
    print(i)

print()
for i in range(7, 35, 7):
    print(i)

print()
for i in range(5, 0, -1):
    print(i)

print()
for i in range(20, 0, -4):
    print(i)

print()
import random  # here random is a MODULE & randint is a FUNCTION in random module

for i in range(5):
    print(random.randint(1, 10))


print()
import sys              #using sys.exit()

while True:
    print("Enter exit to exit")
    spam = input()
    if spam == 'exit':
        sys.exit()
    else:
        print("You typed " + spam)

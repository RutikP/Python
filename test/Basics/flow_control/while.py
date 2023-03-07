spam = 0
while spam < 5:
    print("Hello World!!")
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name')
    name = input()

print("Thank You!!")
print()
print()
#  Using break
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
#  Using continue
while True:
    print("Please enter your name")
    name = input()
    if name != 'Rutik':
        continue
    print("Hello Rutik!! What is ur password?")
    password = input()
    if password != "rutik@8050":
        print("Wrong Password!!")
    else:
        print("Access granted!!")
    break

print()
i = 1
while i < 11:
    print(i)
    i = i + 1

print()
def count():
    ct = 10
    while ct > 0:
        print(ct, end=" ")
        ct = ct - 1
count()
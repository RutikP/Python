print("Enter your name")
name = input()
if name == "Rutik":
    print("Hello Rutik!")
else:
    print("Hello stranger!")
print("What is your age")
age = input()
age = int(age)
if age < 12:
    print("Ohh then your not "+name+" your kiddo hahahaha!!!")
elif age > 12:
     print("Your a gentelman "+name)
else:
    print("Nice to meet you "+name)


while True:
 print('Please type your name.')
 name = input()
 if name == 'your name':
  break
print('Thank you!')

print()
print("Enter the value to store it in spam")
spam = input()
spam = int(spam)
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!!")

    # if your program is stuck in infinite loop then to come out from that press ctrl+
print()


def area(type_, X):
    if type_ == "circle":
        area = 3.14*X**2
        print(area)
    elif type_ == "square":
        area = X*X
        print(area)


area("square", 3)




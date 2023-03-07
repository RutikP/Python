import random
n = 20
to_be_guessed = int(n*random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("It's too large")
        elif guess < to_be_guessed:
            print("It's too small")
    else:
        print("Sorry that you are giving Up!!")
        break
else:
    print("Congratulation. You made it!!")

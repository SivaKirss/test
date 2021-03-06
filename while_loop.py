import random

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("new number:"))
    if guess > 0:
        if guess > to_be_guessed:
            print("number is too large")

        elif guess < to_be_guessed:
            print("number is too small", to_be_guessed)
    else:
        print("Sorry that you have giving up !!!")
        break
else:
    print("Contratulation you have made it !!!")
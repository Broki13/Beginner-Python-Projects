import random

number = random.randint(1, 100)
print("Program generates a number from 1 to 100. What number is it? ")


def get_input():
    global guess
    guess = input()
    guess = int(guess)
    check_numbers()
    if guess > 100:
        print("Number can't be bigger than 100. Try a new number.")
        get_input()
    elif guess < 1:
        print("Number can't be smaller than 1. Try a new number.")
        get_input()


def check_numbers():
    if guess == number:
        print("Congratulations, you guessed.")
        exit()
    else:
        if guess > number:
            print("Too big. Try a new number.")
            get_input()
        else:
            print("Too small. Try a new number.")
            get_input()


get_input()

check_numbers()

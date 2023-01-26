import random


def roll_the_dice():
    number = random.randint(1, 6)
    print(f"The dice shows {number}.")
    print("Do you want to roll again? Y/N ")
    answer = input()
    answer = answer.lower()
    if answer == "y":
        roll_the_dice()
    else:
        print("Closing the program...")
        exit()


roll_the_dice()

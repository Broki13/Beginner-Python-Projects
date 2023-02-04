import random

# try stuff to know how many times to repeat, generator to choose a random word from words list
try_current = 0
try_max = 7
n = 0
generator = random.randint(0, 3)
words = ["jazz", "violin", "elephant", "pringles"]

# answer is the chosen word from the list
answer = words[generator]
print(answer)

# counting the length of the answer to know how many underlines to add
length = len(answer)
word_length = length - 1

# creating underline variable
underline = ""

# setting underline length
while True:
    length -= 1
    underline += "_"
    if length == 0:
        break

# accepting answers and updating underline until player runs out of tries
while True:
    # setting another try
    try_current += 1
    # set player's guess
    guess = input("Type in a letter: ")
    # compare guess with the answer
    while True:
        if answer[n] == guess:
            answer[n] = guess
            n += 1
        if n > word_length:
            break
    if try_current > try_max:
        print("You lost.")
        break


"""
while True:
    while True:
        if guess == answer[n]:
            answer[n] = guess
            n += 1
        else:
            print("Keep trying.")
            
            
    guess = input("\nType in your guess: ")
    try_current += 1
    if try_current > try_max:
        print("You lost.")
        break
"""



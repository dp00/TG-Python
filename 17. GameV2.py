#
# Game V2
# Slide 39
#

from random import randint

secret_number = randint(1, 10)

while True:
    guess = input("Pick a number between 1 and 10? ")

    if secret_number == int(guess):
        print("Yay! You got it.")
        break
    else:
        print("No, that's not it.")

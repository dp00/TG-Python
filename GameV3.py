from random import randint

secret_number = randint(1, 10)

while True:
    guess = input("Pick a number between 1 and 10 ")

    if secret_number == int(guess):
        print("Yay! You got it.")
        break
    elif secret_number > int(guess):
        print("No, that's too low.")
    else:
        print("No, that's too high.")


# Game 1

secret_number = 7

guess = input("What number am I thinking of? ")

if int(guess) == secret_number:
    print("Yay! You got it.")
else:
    print("No, that's not it.")
    print(secret_number)

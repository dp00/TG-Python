#
# Game 1
# Slide 37
#
secret_number = 7

guess = int(input("What number am I thinking of? "))

if int(guess) == secret_number:
    print("Yay! You got it.")
else:
    print("No, that's not it.")
    print(secret_number)

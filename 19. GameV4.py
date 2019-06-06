# --------------------- cut here ----------------------------------
# limiting the number of guesses

from random import randint

secret_number = randint(1, 10)

# Number of guesses left
guesses_left = 5  

while guesses_left > 0:
    guess = input("Pick a number between 1 and 10 ")

# we subtract / decrement 1 each iteration we can also write this as guesses_left -= 1
    guesses_left =  guesses_left  - 1
    
    if secret_number == int(guess):
        print("Yay! You got it.")
        break
    elif secret_number > int(guess):
        print("No, that's too low.")
    else:
        print("No, that's too high.")
        
# You’ve lost. Game Over
    if(guesses_left == 0):
        print("You're out of guesses, the number was "+str(secret_number))

# --------------------- cut here ----------------------------------

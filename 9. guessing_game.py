# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (_Hint: remember to use the user input lessons from the very first exercise

# Extras:

#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.


# Solution:

import random
numbers = range(10)
number = random.choice(numbers)
count = 0
while True:
    guess = input('Enter a number from 1 to 9: ')
    if guess == 'exit':
        break
    guess = int(guess)
    count += 1
    if guess == number:
        print('You guessed exactly right!')
        print(f'You took {count} guesses.')
    elif guess < number:
        print('You guessed too low')
    else:
        print('You guessed too high')

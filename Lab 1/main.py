# Author: Aiden Perkins & Joshua Nwabuzor
# Date: August 23rd, 2023
# Description: Guessing game to guess a number between 1 to 100.


import check_input
import random

def main():
    r = random.randint(1, 100)
    count = 0
    print('I\'m thinking of a number.', end=' ')
    guess = check_input.get_int_range('Make a guess (1-100):', 1, 100)
    while guess != r:
        if count != 0:
            guess = check_input.get_int_range('Guess again (1-100):', 1, 100)
        if guess > r:
            guess = print('Too high!', end=' ')
            count += 1
        elif guess < r:
            guess = print('Too low!', end=' ')
            count += 1
    count += 1
    print(f'Correct! You got it in {count} tries.')

    
if __name__ == '__main__':
    main()
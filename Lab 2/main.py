# Name:Aiden Perkins & Joshua Nwabuzor
# Date: August 28th. 2023
# Description: Allows a user to play three card monte, player has to place a bet, then guess which of three cards is the queen, the bet is doubled if they guess correctly, and they lose they money if they get it wrong.

import check_input
import random


def get_users_bet(money: int) -> int:
    """Shows the user the amount of money they have and asks how much they want to bet.

    Args:
        money (int): The users current money.

    Returns:
        int: The amount of money the user wants to bet.
    """    
    print(f'You have ${money}.')
    return check_input.get_int_range('How much you wanna bet? ', 1, money)


def get_users_choice() -> int:
    """Prints 3 cards and asks for the users choice.

    Returns:
        int: The users guess between 1 & 3.
    """
    print('+-----+ +-----+ +-----+')
    print('|     | |     | |     |')
    print('|  1  | |  2  | |  3  |')
    print('|     | |     | |     |')
    print('+-----+ +-----+ +-----+')
    return check_input.get_int_range('Find the queen. ', 1, 3)


def display_queen_loc(queen_loc: int):
    """Displays the cards and which is the queen.
    
    Args:
        queen_loc (int): The queens location between 1 & 3.
    """    
    loc = 'KKK'  # 😨
    loc = loc[0:queen_loc - 1] + 'Q' + loc[queen_loc:]
    print('+-----+ +-----+ +-----+')
    print('|     | |     | |     |')
    print(f'|  {loc[0:1]}  | |  {loc[1:2]}  | |  {loc[2:3]}  |')
    print('|     | |     | |     |')
    print('+-----+ +-----+ +-----+')


def main():
    """Loops asking the user if they want to bet, which choice, and explains if they were right or wrong, and asks if they want to continue."""
    users_money = 100
    print('-Three card Monte-')
    print('Find the queen to double your bet')
    print()
    while users_money > 0:
        location = random.randint(1, 3)
        bet = get_users_bet(users_money)
        choice = get_users_choice()
        display_queen_loc(location)
        if choice == location:
            print('You got Lucky this time...')
            users_money += bet
        else:
            print('Sorry... you lose.')
            users_money -= bet
        if input('Play again? (Y/N): ').lower() == 'n':
            break
    if users_money == 0:
        print('You\'re out of money. Beat it loser!')


if __name__ == '__main__':
    main()

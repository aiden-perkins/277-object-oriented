# Names: Aiden Perkins & Joshua Nwabuzor
# Date: October 2nd, 2023
# Description:
import check_input
from deck import Deck
from player import Player
from dealer import Dealer


def display_winner(pScore: int, dScore: int, points: list[int]) -> None:
    """Displays the winner of the round based on the player’s and dealer’s hand scores.

    Args:
        pScore (int): The score of the player.
        dScore (int): The score of the dealer
        points (list[int]): A list of size 2 that holds the points for the player and dealer respectively.
    """
    if (pScore > 21 and dScore > 21) or pScore == dScore:
        print("Tie")
    elif pScore > 21 or (dScore <= 21 and dScore > pScore):
        print('Dealer wins.')
        points[1] += 1
    else:
        print('Player wins.')
        points[0] += 1
    print(f'Player\'s points: {points[0]}')
    print(f'Dealer\'s points: {points[1]}')


def main() -> None:
    """Plays the blackjack game by repeatedly asking the player to play, and during each round if they want to hit or stay."""
    print('-Blackjack-')
    points = [0, 0]
    deck = Deck()
    deck.shuffle()
    while True:
        if len(deck) < 15:
            deck = Deck()
            deck.shuffle()
        player = Player(deck)
        print(f'\nPlayer\'s Cards:\n{player}')
        option = 0
        while option != 2:
            option = check_input.get_int_range('1. Hit\n2. Stay\nEnter choice: ', 1, 2)
            if option == 1:
                player.hit()
                print(f'\nPlayer\'s Cards:\n{player}')
            if player.score() > 21:
                print('Bust!')
                break
        dealer = Dealer(deck)
        print(dealer.play())
        display_winner(player.score(), dealer.score(), points)
        if not check_input.get_yes_no('Play again? (Y/N): '):
            break

if __name__ == '__main__':
    main()

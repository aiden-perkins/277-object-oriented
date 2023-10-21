# Names: Aiden Perkins & Joshua Nwabuzor
# Date: September 9th, 2023
# Description: A Program that let's two players partake in ship, captain, and crew! 3 dice are rolled for each players turn, and they need to get 6, 5, and 4 in that order to get cargo points to win.
import random

def roll_dice(dice: list[int]) -> None:
    """Randomizes the numbers in the given list between 1 & 6.
    
    Args:
        dice (list[int]): A list of numbers that can be any length.
    """
    dice[:] = sorted((random.randint(1,6) for _ in dice), reverse=True)

def display_dice(name: str, dice: list[int]) -> None:
    """Displays the given list of numbers with the name.
    
    Args:
        name (str): The name of the list to be printed.
        dice (list[dice]): A list of numbers that can be any length.
    """
    print(f'{name} = {" ".join([str(die) for die in dice])}')

def find_winner(player_points: list[int]) -> None:
    """Prints the 2 players points and displays who won.
    
    Args:
        player_points (list[int]): A list with 2 numbers between 0 and 12 that represents the 2 players points.
    """
    print(f'Score:\nPlayer #1 = {player_points[0]}\nPlayer #2 = {player_points[1]}')
    if player_points[0] == player_points[1]:
        return print("Oh no, Shiver me Timbers! We have a Tie!")
    print(f'Player #{player_points.index(max(player_points)) + 1} won!')

def main() -> None:
    """Allows 2 players to play the ship, captain, and crew game with 5 dice."""
    print('- Ship, Captain, and Crew! -\n')
    points = []
    for player_num in [1, 2]:
        print(f'Player #{player_num}\'s Turn:')
        dice = [0, 0, 0, 0, 0]
        keep = []
        for roll_num in [1, 2, 3]:
            roll_dice(dice)
            display_dice('Roll', dice)
            for _ in range(len(dice)):
                if len(keep) == 0 and 6 in dice:
                    print('Yo ho ho! Ye secured a ship!')
                    keep.append(dice.pop(dice.index(6)))
                if len(keep) == 1 and 5 in dice:
                    print('Shiver me timbers! A Capt’n')
                    keep.append(dice.pop(dice.index(5)))
                if len(keep) == 2 and 4 in dice:
                    print('Ye bribed a crew with Grog!')
                    keep.append(dice.pop(dice.index(4)))
            display_dice('Keep', keep)
            if len(dice) == 2:
                display_dice('Cargo', dice)
                print(f'Your cargo points are: {sum(dice)}')
            if roll_num != 3 and input('\nRoll again? ').lower() == 'n':
                break
        print(f'Player #{player_num} points = {({3: sum(dice)}.get(len(keep), 0))}\n')
        points.append({3: sum(dice)}.get(len(keep), 0))
    find_winner(points)

if __name__ == '__main__':
    main()

import random

def roll_dice_F(dice):
    for i in range(len(dice)):
        dice[i] = random.randint(1, 6)
    dice.sort(reverse=True)

def display_dice(name, dice):
    print(name + ':', ' '.join(map(str, dice)))

def find_winner(player_points):
    print('Player 1 points:', player_points[0])
    print('Player 2 points:', player_points[1])
    if player_points[0] > player_points[1]:
        print('Player 1 wins!')
    elif player_points[0] < player_points[1]:
        print('Player 2 wins!')
    else:
        print('It\'s a tie!')

def main():
    player_scores = [0, 0]
    keep_dice = []
    roll_dice = [0, 0, 0, 0, 0]
    for player in range(2):
        print('Player', player + 1)
        keep_dice.clear()
        for i in range(3):
            roll_dice_F(roll_dice)
            display_dice('Roll', roll_dice)
            if 6 in roll_dice and 6 not in keep_dice:
                keep_dice.append(6)
                roll_dice.remove(6)
            if 5 in roll_dice and 5 not in keep_dice and 6 in keep_dice:
                keep_dice.append(5)
                roll_dice.remove(5)
            if 4 in roll_dice and 4 not in keep_dice and 5 in keep_dice:
                keep_dice.append(4)
                roll_dice.remove(4)
            display_dice('Keep', keep_dice)
            if len(keep_dice) == 3:
                cargo_score = sum(roll_dice)
                while True:
                    choice = input('Roll again for higher cargo (y/n)? ')
                    if choice.lower() == 'y':
                        roll_dice(roll_dice)
                        display_dice('Roll', roll_dice)
                        cargo_score = sum(roll_dice)
                    else:
                        break
                player_scores[player] = cargo_score
                break
    find_winner(player_scores)

main()

# Names: Aiden Perkins & Joshua Nwabuzor
# Date: October 11th, 2023
# Description: A game where the user must defeat three dragons to pass the trials.
from hero import Hero
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from dragon import Dragon
import check_input
import random


def main() -> None:
    """Creates a hero object from the users given name and continusouly asks the user which dragon they want to attack
    and with what weapon."""
    hero = Hero(input('What is your name, challenger?\n'), 50)
    print(f'Welcome to dragon training, {hero.name}\nYou must defeat 3 dragons.\n')
    dragons = [Dragon('Deadly Nadder', 10), FireDragon('Gronckle', 15, 3), FlyingDragon('Timberjack', 20, 3)]
    while len(dragons) > 0 and hero.hp > 0:
        print(hero)
        [print(f'{i + 1}. Attack {dragon}') for i, dragon in enumerate(dragons)]
        drgn_c = check_input.get_int_range('Choose a dragon to attack: ', 1, len(dragons)) - 1
        print('\nAttack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)')
        atk_c = check_input.get_int_range('Enter weapon: ', 1, 2)
        print()
        print([hero.basic_attack, hero.special_attack][atk_c - 1](dragons[drgn_c]))
        if dragons[drgn_c].hp <= 0:
            dragons.pop(drgn_c)
        if len(dragons) != 0:
            r = random.randint(0, len(dragons) * 2 - 1)
            print([dragons[r // 2].basic_attack, dragons[r // 2].special_attack][r % 2](hero))
        print()
    if hero.hp < 1:
        print('You died.')
    if len(dragons) == 0:
        print('Congratulations! You have defeated all 3 dragons, you have passed the trials.')


if __name__ == '__main__':
    main()

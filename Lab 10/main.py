# Names: Aiden Perkins & Joshua Nwabuzor
# Date: October 30th, 2023
# Description: Has the user wander through a haunted dungeon maze and fight monsters that they encounter as they explore. The user wins if they reach the dungeon’s exit alive.
import check_input
import random
from hero import Hero
from map import Map
from enemy import Enemy


def main() -> None:
    """Prompts the user to enter their name and creates a loop that repeats until the hero dies, the hero finds the finish, or the user quits the game."""
    name = input('What is your name, traveler? ')
    hero = Hero(name)
    hero_max_hp = hero.hp
    dungeon_map = Map()
    while hero.hp > 0:
        print(hero)
        print(dungeon_map.show_map(hero.loc))
        print('1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit')
        option = check_input.get_int_range('Enter choice: ', 1, 5) - 1
        if option == 4:
            break
        go_x = [hero.go_north, hero.go_south, hero.go_east, hero.go_west]
        map_encounter = go_x[option]()
        if map_encounter == 'o':
            print('You cannot go that way...\n')
            continue
        dungeon_map.reveal(hero.loc)
        if map_encounter == 'n':
            print('There is nothing here...')
        elif map_encounter == 's':
            print('This is the start of the map.')
        elif map_encounter == 'm':
            monster = Enemy()
            print('You encounter a ', end='')
            print(monster)
            while monster.hp > 0 and hero.hp > 0:
                print(f'1. Attack {monster.name}')
                print(f'2. Run Away')
                option = check_input.get_int_range('Enter choice: ', 1, 2)
                if option == 1:
                    print(hero.attack(monster))
                    if monster.hp > 0:
                        print(monster.attack(hero))
                    else:
                        print(f'You have slain a {monster.name}')
                        dungeon_map.remove_at_loc(hero.loc)
                if option == 2:
                    new = 'o'
                    while new == 'o':
                        new = go_x[random.randint(0, 3)]()
                    dungeon_map.reveal(hero.loc)
                    break
        elif map_encounter == 'i':
            if hero.hp == hero_max_hp:
                print('You found a Health Potion, but you\'re at the max HP already...')
            else:
                print('You found a Health Potion!')
                hero.heal()
                dungeon_map.remove_at_loc(hero.loc)
        elif map_encounter == 'f':
            print('Congratulations! You found the exit.')
            break
        print()
    print('Game Over')


if __name__ == '__main__':
    main()

# Names: Aiden Perkins & Joshua Nwabuzor
# Date: October 16th, 2023
# Description: Simulates an escape room by having the user open a series of three doors randomly chosen from several different types of doors.
import check_input
from basic_door import BasicDoor
from deadbolt_door import DeadboltDoor
from locked_door import LockedDoor
from door import Door
import random

def open_door(door: Door) -> None:
    """Prompts the user to try and open the door.

    Args:
        door (Door): The door the user is trying to open.
    """
    print(door.examine_door())
    while True:
        print(door.attempt(check_input.get_int_range(door.menu_options(), 1, door.get_menu_max())))
        if door.is_unlocked():
            print(door.success())
            break
        print(door.clue())

def main() -> None:
    """Randomly selects 3 doors for the user to try and open."""
    print('Welcome to the Escape Room. You must unlock 3 doors to escape...\n')
    doors = [BasicDoor, DeadboltDoor, LockedDoor]
    for _ in range(3):
        open_door(doors[random.randint(0, 2)]())
    print('Congratulations! You escaped...this time.')

if __name__ == '__main__':
    main()

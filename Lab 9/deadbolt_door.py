from door import Door
import random

class DeadboltDoor(Door):
    """A subclass of Door that represents a door 2 deadbolt locks.

    Attributes:
        _bolt1 (int): The first deadbolt lock.
        _bolt2 (int): The second deadbolt lock.
    """
    def __init__(self) -> None:
        """Initializes both deadbolts to be a random number between 0 & 1."""
        self._bolt1 = random.randint(0, 1)
        self._bolt2 = random.randint(0, 1)

    def examine_door(self) -> str:
        """Returns a string description of the door.

        Returns:
            str: The description of the door.
        """
        return "A door with two deadbolts. Both need to be unlocked to open the door, but you can\'t tell if each one is locked or unlocked."

    def menu_options(self) -> str:
        """Returns a string of the 2 menu options of which deadbolt you want to toggle.

        Returns:
            str: The menu for the door.
        """
        return '1. Toggle Bolt 1\n2. Toggle Bolt 2\n'

    def get_menu_max(self) -> int:
        """Returns the number of options in the menu.

        Returns:
            int: The number of menu options, 2.
        """
        return 2

    def attempt(self, option: int) -> str:
        """Updates the deadbolt the user choose to change & returns a string of their action.

        Args:
            option (int): The option the user choose.

        Returns:
            str: A description of which deadbolt they choose.
        """
        if option == 1:
            self._bolt1 = abs(self._bolt1 - 1)
        if option == 2:
            self._bolt2 = abs(self._bolt2 - 1)
        return f'You toggle the {["first", "second"][option-1]} bolt.'

    def is_unlocked(self) -> bool:
        """Checks to see if the door was unlocked.

        Returns:
            bool: True if both deadbolts are unlocked, false otherwise.
        """
        return self._bolt1 == 1 and self._bolt2 == 1

    def clue(self) -> str:
        """Returns if one or both of the deadbolts are locked.

        Returns:
            str: The string of how many of the deadbolts are unlocked.
        """
        if self._bolt1 == 1 or self._bolt2 == 1:
            return 'You jiggle the door... it seems like one of the bolts is unlocked.'
        return 'You jiggle the door... it seems like it\'s completely locked.'


    def success(self) -> str:
        """Returns the congratulatory message when the user was successful.

        Returns:
            str: A congratulatory message.
        """
        return 'You unlocked both deadbolts and opened the door.\n'

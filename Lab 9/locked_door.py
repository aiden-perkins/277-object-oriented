from door import Door
import random

class LockedDoor(Door):
    """A subclass of Door that represents a door with a key in a random location.

    Attributes:
        _key_location (int): The location of the key, between 1 & 3.
        _input (int): The user's last guess of where the key is.
    """
    def __init__(self) -> None:
        """Initializes the _key_location to be a random number between 1 & 3, and _input as 0."""
        self._key_location = random.randint(1, 3)
        self._input = 0

    def examine_door(self) -> str:
        """Returns a string description of the door.

        Returns:
            str: The description of the door.
        """
        return 'A locked door.\nLook around for the key.'

    def menu_options(self) -> str:
        """Returns a string of the 3 menu options that ask the user where they want to look.

        Returns:
            str: The menu for the door.
        """
        return '1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock.\n'

    def get_menu_max(self) -> int:
        """Returns the number of options in the menu.

        Returns:
            int: The number of menu options, 3.
        """
        return 3

    def attempt(self, option: int) -> str:
        """Updates the _input variable to what the user choose and returns a message about it.

        Args:
            option (int): The option the user choose.

        Returns:
            str: A description of where they looked.
        """
        self._input = option
        return f'You looked under the {["mat", "flower pot", "fake rock"][option - 1]}.'

    def is_unlocked(self) -> bool:
        """Checks to see if the door was unlocked.

        Returns:
            bool: True if the _key_location matches _input, false otherwise.
        """
        return self._key_location == self._input

    def clue(self) -> str:
        """Tells the user to look somewhere else.

        Returns:
            str: Where to look next.
        """
        return 'Look somewhere else'

    def success(self) -> str:
        """Returns the congratulatory message when the user was successful.

        Returns:
            str: A congratulatory message.
        """
        return 'Congratulations, you opened the door.\n'

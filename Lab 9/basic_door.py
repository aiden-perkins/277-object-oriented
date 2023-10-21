from door import Door
import random

class BasicDoor(Door):
    """A subclass of Door that represents a door that is either push or pull.

    Attributes:
        _state (int): If the door is either push or pull.
        _input (int): The user's last guess of if it is push or pull.
    """
    def __init__(self) -> None:
        """Initializes the _state to be a random number between 1 & 2, and _input as 0."""
        self._state = random.randint(1, 2)
        self._input = 0

    def examine_door(self) -> str:
        """Returns a string description of the door.

        Returns:
            str: The description of the door.
        """
        return 'A door that is either pushed or pulled.'

    def menu_options(self) -> str:
        """Returns a string of if the user wants to push or pull the door.

        Returns:
            str: The menu for the door.
        """
        return '1. Push\n2. Pull\n'

    def get_menu_max(self) -> int:
        """Returns the number of options in the menu.

        Returns:
            int: The number of options, 2.
        """
        return 2

    def attempt(self, option: int) -> str:
        """Attempts what the user choose to do and changes _input.

        Args:
            option (int): The option the user choose.

        Returns:
            str: A description of if the user pushed or pulled the door.
        """
        self._input = option
        return f'You {["push", "pull"][option - 1]} the door.'

    def is_unlocked(self) -> bool:
        """Checks to see if the user pushed or pulled correctly.

        Returns:
            bool: True if they did, false otherwise.
        """
        return self._state == self._input

    def clue(self) -> str:
        """Returns the hint if the user did the wrong option.

        Returns:
            str: The hint for opening the door.
        """
        return 'Try the other way.'

    def success(self) -> str:
        """Returns the congratulatory message when the user was successful.

        Returns:
            str: A congratulatory message.
        """
        return 'Congratulations, you opened the door.\n'
import abc

class Door(abc.ABC):
    """An interface the has multiple functions that allow the user to interact with the door in various ways."""

    @abc.abstractmethod
    def examine_door(self) -> str:
        """Returns a string description of the door.

        Returns:
            str: The description of the door.
        """
        pass

    @abc.abstractmethod
    def menu_options(self) -> str:
        """Returns a string of the menu options that user can choose from when attempting to unlock the door.

        Returns:
            str: The menu for the door.
        """
        pass

    @abc.abstractmethod
    def get_menu_max(self) -> int:
        """Returns the number of options in the menu.

        Returns:
            int: The max amount of menu options.
        """
        pass

    @abc.abstractmethod
    def attempt(self, option: int) -> str:
        """Attempts what the user choose to do and changes the appropriate variables.

        Args:
            option (int): The option the user choose.

        Returns:
            str: A description of the option they choose.
        """
        pass

    @abc.abstractmethod
    def is_unlocked(self) -> bool:
        """Checks to see if the door was unlocked.

        Returns:
            bool: True if it is, false otherwise.
        """
        pass

    @abc.abstractmethod
    def clue(self) -> str:
        """Returns the hint if the user was unsuccessful at their attempt.

        Returns:
            str: The hint for opening the door.
        """
        pass

    @abc.abstractmethod
    def success(self) -> str:
        """Returns the congratulatory message when the user was successful.

        Returns:
            str: A congratulatory message.
        """
        pass


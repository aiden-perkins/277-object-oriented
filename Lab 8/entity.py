import abc


class Entity(abc.ABC):
    """A abstract class that represents a entity with a basic & special attack.
    
    Attributes:
        _name (str): Name of the entity.
        _max_hp (int): Max HP of the entity.
        _hp (int): HP of the entity.
    """

    def __init__(self, name: str, max_hp: int) -> None:
        """Initializes the name & max HP of the entity.

        Args:
            name (str): Name of the entity.
            max_hp (int): Max HP of the entity.
        """
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def hp(self) -> int:
        """Returns the entities hp."""
        return self._hp

    @property
    def name(self) -> str:
        """Returns the entities name."""
        return self._name

    def take_damage(self, dmg: int) -> None:
        """Removes health points from the entity.

        Args:
            dmg (int): the amount of dmg the entity takes
        """
        self._hp -= min(dmg, self._hp)

    def __str__(self) -> str:
        """Builds a string that contains the name, hp, and max hp of the entity.

        Returns:
            str: The final built string with the name, hp, & max hp.
        """
        return f'{self._name}: {self._hp}/{self._max_hp}'

    @abc.abstractmethod
    def basic_attack(self, other: 'Entity') -> str:
        """Basic Attack to be implemented in child classes."""
        pass

    @abc.abstractmethod
    def special_attack(self, other: 'Entity') -> str:
        """Special Attack to be implemented in child classes."""
        pass

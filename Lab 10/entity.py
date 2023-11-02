import abc


class Entity(abc.ABC):
    """An abstract class that describes a character in the game.
    
    Attributes:
        _name (str) = The name of the entity.
        _hp (int) = The hp of the entity.
        _max_hp (int) = The max hp of the entity.
    """
    def __init__(self, name: str, max_hp: int) -> None:
        """Initializes each of the instance variables.

        Args:
            name (str): The name of the entity.
            max_hp (int): The max hp of the entity.
        """
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp

    @property
    def name(self) -> str:
        """Returns the name."""
        return self._name
        
    @property
    def hp(self) -> int:
        """Returns the hp."""
        return self._hp

    def __str__(self) -> str:
        """Returns a string with the name, hp, and max hp.

        Returns:
            str: The information about the entity.
        """
        return f'{self._name}\nHP: {self._hp}/{self._max_hp}'

    def take_damage(self, dmg: int) -> None:
        """Subtracts the dmg from the hp, but does not allow the hp to drop below 0.

        Args:
            dmg (int): The damage the entity takes.
        """
        self._hp -= min(dmg, self._hp)

    def heal(self) -> None:
        """Sets the entities hp to its max hp."""
        self._hp = self._max_hp
    
    @abc.abstractmethod
    def attack(self, entity: 'Entity') -> None:
        """For subclasses to override to attack and do damage to the opposing entity.

        Args:
            entity (Entity): The entity to attack.
        """
        pass



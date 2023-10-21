from dragon import Dragon
from entity import Entity
import random


class FlyingDragon(Dragon):
    """A class that represents a flying dragon which inherits from dragon and adds swoops as a special attack.

    Attributes:
        _swoops (int): The number of swoops the flying dragon can make.
    """

    def __init__(self, name: str, max_hp: int, swoops: int) -> None:
        """Initializes the name, max HP, and swoops of the flying dragon.

        Args:
            name (str): Name of the flying dragon.
            max_hp (int): Max HP of the flying dragon.
            swoops (int): The number of swoops the flying dragon can make.
        """
        super().__init__(name, max_hp)
        self._swoops = swoops

    def special_attack(self, other: Entity) -> str:
        """The special attack for the flying dragon limited by the amount of swoops.

        Args:
            other (Entity): The entity that will take damage from this attack.

        Returns:
            str: A string that contains which entity they attacked and how much damage.
        """
        if self._swoops != 0:
            dmg = random.randint(5, 8)
            other.take_damage(dmg)
            self._swoops -= 1
            return f'{self.name} swoops at you for {dmg} damage!'
        return f'{self.name} tries to swoop down to hit you, but failed.'

    def __str__(self) -> str:
        """Adds the number of swoops remaining to the entities description.

        Returns:
            str: A string the has the name, HP, and swoops.
        """
        return super().__str__() + "\nSwoops Remaining: " + str(self._swoops)

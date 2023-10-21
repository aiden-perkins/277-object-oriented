from dragon import Dragon
from entity import Entity
import random


class FireDragon(Dragon):
    """A class that represents a fire dragon which inherits from dragon and adds fire shots as a special attack.

    Attributes:
        _f_shots (int): The number of fire shots the fire dragon can make.
    """

    def __init__(self, name: str, max_hp: int, f_shots: int) -> None:
        """Initializes the name, max HP, and fire shots of the fire dragon.

        Args:
            name (str): Name of the flying dragon.
            max_hp (int): Max HP of the flying dragon.
            f_shots (int): The number of fire shots the fire dragon can make.
        """
        super().__init__(name, max_hp)
        self._f_shots = f_shots

    def special_attack(self, other: Entity) -> str:
        """The special attack for the fire dragon limited by the amount of fire shots.

        Args:
            other (Entity): The entity that will take damage from this attack.

        Returns:
            str: A string that contains which entity they attacked and how much damage.
        """
        if self._f_shots != 0:
            dmg = random.randint(5, 8)
            other.take_damage(dmg)
            self._f_shots -= 1
            return f'{self.name} engulfs you in flames for {dmg} damage!'
        return f'{self.name} tries to spit fire at you but is all out of fire shots.'

    def __str__(self) -> str:
        """Adds the number of fire shots remaining to the entities description.

        Returns:
            str: A string the has the name, HP, and fire shots.
        """
        return super().__str__() + "\nFire Shots remaining " + str(self._f_shots)

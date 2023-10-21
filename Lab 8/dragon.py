import random
from entity import Entity


class Dragon(Entity):
    """A class that represents a dragon which inherits from entity."""

    def basic_attack(self, other: Entity) -> str:
        """The  for thebasic attack dragon.

        Args:
            other (Entity): The entity that will take damage from this attack.

        Returns:
            str: A string that contains which entity they attacked and how much damage.
        """
        dmg = random.randint(3, 7)
        other.take_damage(dmg)
        return f'{self.name} smashes you with its tail for {dmg} damage!'

    def special_attack(self, other: Entity) -> str:
        """The special attack for the dragon.

        Args:
            other (Entity): The entity that will take damage from this attack.

        Returns:
            str: A string that contains which entity they attacked and how much damage.
        """
        dmg = random.randint(4, 8)
        other.take_damage(dmg)
        return f'{self.name} slashes you with its claws for {dmg} damage!'

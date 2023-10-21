import random
from entity import Entity


class Hero(Entity):
    """A class that represents the hero that inherits everything from Entity and creates its own special/.
   basic attacks """

    def basic_attack(self, other: Entity) -> str:
        """Attacks the given entity with (1-6) + (1-6) damage.

        Args:
            other (Entity): The entity that will take damage from this attack.

        Returns:
            str: A string that contains which entity they attacked and how much damage.
        """
        dmg = random.randint(1, 6) + random.randint(1, 6)
        other.take_damage(dmg)
        return f'You slash the {other.name} with your sword for {dmg} damage.'

    def special_attack(self, other: Entity) -> str:
        """Attacks the given entity with (1-12) damage.

        Args:
            other (Entity): The entity that will take damage from this attack.

        Returns:
            str: A string that contains which entity they attacked and how much damage.
        """
        dmg = random.randint(1, 12)
        other.take_damage(dmg)
        return f'You hit the {other.name} with an arrow for {dmg} damage'

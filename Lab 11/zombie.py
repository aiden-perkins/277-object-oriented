from entity import Entity
import random


class Zombie(Entity):
    """A zappy zombie entity that is the expert level of difficulty."""

    def __init__(self) -> None:
        """Creates a zappy zombie entity with the health between 8 & 10."""
        super().__init__('Zappy Zombie', random.randint(8, 10))

    def attack(self, entity) -> str:
        """Attacks the entity with damage between 5 & 12.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            str: A string representing the event that occured.
        """
        damage = random.randint(5, 12)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'
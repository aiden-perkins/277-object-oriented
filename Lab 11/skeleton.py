from entity import Entity
import random


class Skeleton(Entity):
    """A spooky skeleton entity that is the expert level of difficulty."""

    def __init__(self) -> None:
        """Creates a spooky skeleton entity with the health between 6 & 10."""
        super().__init__('Spooky Skeleton', random.randint(6, 10))

    def attack(self, entity: Entity) -> str:
        """Attacks the entity with damage between 6 & 10.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            str: A string representing the event that occured.
        """
        damage = random.randint(6, 10)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'
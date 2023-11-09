from entity import Entity
import random


class EasyGoblin(Entity):
    """A goblin entity that is the easy level of difficulty."""

    def __init__(self) -> None:
        """Creates a goblin entity with the health between 4 & 6."""
        super().__init__('Goblin', random.randint(4, 6))

    def attack(self, entity: Entity) -> str:
        """Attacks the entity with damage between 2 & 5.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            str: A string representing the event that occured.
        """
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'
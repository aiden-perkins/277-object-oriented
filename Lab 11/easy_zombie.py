from entity import Entity
import random


class EasyZombie(Entity):
    """A zombie entity that is the easy level of difficulty."""

    def __init__(self) -> None:
        """Creates a zombie entity with the health between 4 & 5."""
        super().__init__('Zombie', random.randint(4, 5))

    def attack(self, entity: Entity) -> str:
        """Attacks the entity with damage between 1 & 5.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            str: A string representing the event that occured.
        """
        damage = random.randint(1, 5)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'
from entity import Entity
import random


class Goblin(Entity):
    """A gigantic goblin entity that is the expert level of difficulty."""
    
    def __init__(self) -> None:
        """Creates a gigantic goblin entity with the health between 8 & 12."""
        super().__init__('Gigantic Goblin', random.randint(8, 12))

    def attack(self, entity: Entity) -> str:
        """Attacks the entity with damage between 6 & 12.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            str: A string representing the event that occured.
        """
        damage = random.randint(6, 12)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'
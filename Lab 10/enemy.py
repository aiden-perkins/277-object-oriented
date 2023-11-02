from entity import Entity
import random


class Enemy(Entity):
    """Extends entity - monster character that the hero encounters in the maze."""
    def __init__(self) -> None:
        """Randomizes a name from a list of names and randomizes the monster's hp (4-8)."""
        names = ['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie']
        super().__init__(names[random.randint(0, 4)], random.randint(4, 8))

    def attack(self, entity: Entity) -> str:
        """Enemy attacks hero - random damage in the range 1-4.

        Args:
            entity (Entity): The hero to attack.

        Returns:
            str: A string that represents the event.
        """
        damage = random.randint(1, 4)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'

from entity import Entity
import random


class EasySkeleton(Entity):
    """A skeleton entity that is the easy level of difficulty."""
    
    def __init__(self) -> None:
        """Creates a skeleton entity with the health between 3 & 4."""
        super().__init__('Skeleton', random.randint(3, 4))

    def attack(self, entity: Entity) -> str:
        """Attacks the entity with damage between 1 & 4.
        
        Args:
            entity (Entity): The entity to attack.
            
        Returns:
            str: A string representing the event that occured.
        """
        damage = random.randint(1, 4)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'
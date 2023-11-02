import random
from map import Map
from entity import Entity


class Hero(Entity):
    """Subclass that inherits from Entity, adding a location variable and methods to manipulate that location.

    Attributes:
        _loc (list[int]) = The location of the hero.
    """
    def __init__(self, name: str) -> None:
        """Initializes the name and max_hp using super, sets the hero's starting location to row=0, col=0.

        Args:
            name (str): The name of the hero.
        """
        super().__init__(name, 25)
        self._loc = [0, 0]

    @property
    def loc(self) -> list[int]:
        """Returns the location."""
        return self._loc

    def attack(self, entity: Entity) -> str:
        """Hero attacks the enemy - randomize damage in the range 2-5, and returns a string representing the event.

        Args:
            entity (Entity): The entity the hero should attack.

        Returns:
            str: A string that represents the event.
        """
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return f'{self.name} attacks a {entity.name} for {damage} damage.'
        
    def go_north(self) -> str:
        """Update the hero's location to go north and return that new string if it can, otherwise return 'o'.

        Returns:
            str: Either the spot string or 'o' if we can't go in that direction.
        """
        m = Map()
        if -1 < self._loc[0] - 1:
            self._loc[0] -= 1
            return m[self._loc[0]][self._loc[1]]
        return 'o'
        
    def go_east(self) -> str:
        """Update the hero's location to go east and return that new string if it can, otherwise return 'o'.

        Returns:
            str: Either the spot string or 'o' if we can't go in that direction.
        """
        m = Map()
        if len(m) > self._loc[1] + 1:
            self._loc[1] += 1
            return m[self._loc[0]][self._loc[1]]
        return 'o'

    def go_south(self) -> str:
        """Update the hero's location to go south and return that new string if it can, otherwise return 'o'.

        Returns:
            str: Either the spot string or 'o' if we can't go in that direction.
        """
        m = Map()
        if len(m) > self._loc[0] + 1:
            self._loc[0] += 1
            return m[self._loc[0]][self._loc[1]]
        return 'o'

    def go_west(self) -> str:
        """Update the hero's location to go west and return that new string if it can, otherwise return 'o'.

        Returns:
            str: Either the spot string or 'o' if we can't go in that direction.
        """
        m = Map()
        if -1 < self._loc[1] - 1:
            self._loc[1] -= 1
            return m[self._loc[0]][self._loc[1]]
        return 'o'

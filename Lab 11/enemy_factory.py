import abc 

class EnemyFactory(abc.ABC):
    """An interface for making a enemy factory."""
    
    @abc.abstractmethod
    def create_random_enemy(self):
        """Creates a random entity from the list and returns it."""
        pass
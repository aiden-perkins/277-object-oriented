from enemy_factory import EnemyFactory
from goblin import Goblin
from skeleton import Skeleton
from zombie import Zombie
import random


class ExpertFactory(EnemyFactory):
    """A factory that builds an expert monster."""
    
    def create_random_enemy(self):
        """Returns a random expert monster."""
        return [Goblin, Zombie, Skeleton][random.randint(0, 2)]()
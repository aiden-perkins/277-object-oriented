from enemy_factory import EnemyFactory
from easy_goblin import EasyGoblin
from easy_skeleton import EasySkeleton
from easy_zombie import EasyZombie
import random


class BeginnerFactory(EnemyFactory):
    """A factory that builds an easy monster."""
    
    def create_random_enemy(self):
        """Returns a random easy monster."""
        return [EasyGoblin, EasyZombie, EasySkeleton][random.randint(0, 2)]()
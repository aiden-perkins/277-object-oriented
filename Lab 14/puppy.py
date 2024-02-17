import state_asleep
from puppy_state import PuppyState

class Puppy:
    """A class that represents the puppy."""
    
    def __init__(self):
        """Sets the class variables and its initial state to asleep."""
        self._state = state_asleep.StateAsleep()
        self._plays = 0
        self._feeds = 0

    @property
    def plays(self) -> int:
        """Returns the amount of plays."""
        return self._plays
    
    @property
    def feeds(self) -> int:
        """Returns the amount of feeds."""
        return self._feeds

    def change_state(self, new_state: PuppyState):
        """Changes the puppies state to the given state."""
        self._state = new_state
        self.reset()

    def throw_ball(self) -> str:
        """Attempts to play with the puppy of the current state."""
        return self._state.play(self)

    def give_food(self) -> str:
        """Attempts to eat with the puppy of the current state."""
        return self._state.feed(self)

    def inc_feeds(self):
        """Increases feeds counter."""
        self._feeds += 1

    def inc_plays(self):
        """Increases plays counter."""
        self._plays += 1

    def reset(self):
        """Resets the class variables to 0."""
        self._feeds = 0
        self._plays = 0

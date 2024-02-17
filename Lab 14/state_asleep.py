from puppy_state import PuppyState
import state_eat

class StateAsleep(PuppyState):
    """A class that represents when the puppy is asleep."""
    
    def feed(self, puppy):
        """Changes the puppy to eating.

        Args:
            puppy (Puppy): The puppy we call functions on.

        Returns:
            str: The string for the event that happened.
        """
        puppy.change_state(state_eat.StateEat())
        return 'The puppy wakes up and comes running to eat.'

    def play(self, _puppy):
        """The puppy cannot play while its sleeping.

        Args:
            _puppy (Puppy): The puppy we call functions on.

        Returns:
            str: The string for the event that happened.
        """
        return 'The puppy is asleep. It doesn\'t want to play right now.'

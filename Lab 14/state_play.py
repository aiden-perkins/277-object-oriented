from puppy_state import PuppyState
import state_asleep

class StatePlay(PuppyState):
    """A class that represents when the puppy is playing."""
    
    def feed(self, _puppy) -> str:
        """The puppy cannot eat when it is playing.

        Args:
            _puppy (Puppy): The puppy we call functions on.

        Returns:
            str: The string for the event that happened.
        """
        return 'The puppy is too busy playing with the ball to eat right now.'

    def play(self, puppy) -> str:
        """Plays with the puppy, if the plays is 3 or more it falls asleep.

        Args:
            puppy (Puppy): The puppy we call functions on.

        Returns:
            str: The string for the event that happened.
        """
        puppy.inc_plays()
        s = 'You throw the ball again and the puppy excitedly chases it.'
        if puppy.plays > 2:
            puppy.change_state(state_asleep.StateAsleep())
            return f'{s}\nThe puppy played so much it fell asleep!'
        return s

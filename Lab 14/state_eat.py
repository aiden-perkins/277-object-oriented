from puppy_state import PuppyState
import state_asleep
import state_play

class StateEat(PuppyState):
    """A class that represents when the puppy is eating."""
    
    def feed(self, puppy) -> str:
        """Feeds the puppy, if the puppy eats more then 3 times it falls asleep.

        Args:
            puppy (Puppy): The puppy we call functions on.

        Returns:
            str: The string for the event that happened.
        """
        puppy.inc_feeds()
        s = 'The puppy continues to eat as you add another scoop of kibble to its bowl.'
        if puppy.feeds > 2:
            puppy.change_state(state_asleep.StateAsleep())
            return f'{s}\nThe puppy at so much it fell asleep!'
        return s
            

    def play(self, puppy) -> str:
        """Plays with the puppy after it eats.

        Args:
            puppy (Puppy): The puppy we call functions on.

        Returns:
            str: The string for the event that happened.
        """
        puppy.inc_plays()
        puppy.change_state(state_play.StatePlay())
        return 'The puppy looks up from its food and chases the ball you threw.'

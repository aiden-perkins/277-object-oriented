import abc

class PuppyState(abc.ABC):
    """An interface for the puppies state."""
    
    @abc.abstractmethod
    def play(self, puppy) -> str:
        """The play function for the specific states."""
        pass

    @abc.abstractmethod
    def feed(self, puppy) -> str:
        """The feed function for the specific states."""
        pass
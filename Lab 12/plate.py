import abc

class Plate(abc.ABC):
    """Plate interface that has 4 methods for sub classes to implement."""
    
    @abc.abstractmethod
    def description(self) -> str:
        """The current contents of the plate.

        Returns:
            str: The string that holds the plates description.
        """
        pass

    @abc.abstractmethod
    def area(self) -> int:
        """The area of the plate.

        Returns:
            int: The area the plate can hold.
        """
        pass

    @abc.abstractmethod
    def weight(self) -> int:
        """The weight of the contents of the plate.

        Returns:
            int: The weight the plate can hold.
        """
        pass

    @abc.abstractmethod
    def count(self) -> int:
        """The count of items on the plate.

        Returns:
            int: Number of items on the plate.
        """
        pass

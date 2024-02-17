from plate import Plate
import abc

class PlateDecorator(Plate, abc.ABC):
    """Decorator class that implements the plate interface, stores the old plate and
    calls the new objects methods after the old object.
    
    Attributes:
        _plate (Plate): The old plate object.
    """
    
    def __init__(self, p: Plate) -> None:
        """Sets the _plate attribute to the old plate object.
        
        Args:
            p (plate): The old plate object.
        """
        self._plate = p

    def description(self) -> str:
        """The contents of the old plate.

        Returns:
            str: The string that holds the old plate's description.
        """
        return self._plate.description()

    def area(self) -> int:
        """The area of the old plate.

        Returns:
            int: The area the old plate can hold.
        """
        return self._plate.area()

    def weight(self) -> int:
        """The weight of the contents of the old plate.

        Returns:
            int: The weight the old plate can hold.
        """
        return self._plate.weight()

    def count(self) -> int:
        """The count of items on the old plate.

        Returns:
            int: Number of items on the old plate.
        """
        return self._plate.count()

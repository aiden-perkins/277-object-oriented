from plate import Plate

class SmallPlate(Plate):
    """A class the implements the plate interface."""

    def description(self) -> str:
        """A description of the plate.

        Returns:
            str: The string that holds the plates description.
        """
        return "Sturdy 10 inch paper plate with\n"
        
    def area(self) -> int:
        """The area of the plate.

        Returns:
            int: The area the plate can hold.
        """
        return 78
    
    def weight(self) -> int:
        """The weight of the contents of the plate.

        Returns:
            int: The weight the plate can hold.
        """
        return 32
        
    def count(self) -> int:
        """The count of items on the plate.

        Returns:
            int: Number of items on the plate.
        """
        return 0
        
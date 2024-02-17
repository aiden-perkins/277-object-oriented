from plate_decorator import PlateDecorator

class Pie(PlateDecorator):
    """Inherits the Plate Decorator class to decorate plate objects with a pie."""
    
    def description(self) -> str:
        """The current contents of the plate with a pie.
        
        Returns:
            str: The string that holds the plates description.
        """
        return super().description() + 'Pie and '

    def area(self) -> int:
        """The area of the plate and its contents minus a pie's area.

        Returns:
            int: The area the plate can hold.
        """
        return super().area() - 19

    def weight(self) -> int:
        """The weight of the plate and its contents minus a pie's weight.

        Returns:
            int: The weight the plate can hold.
        """
        return super().weight() - 8

    def count(self) -> int:
        """The count of items on the plate.

        Returns:
            int: Number of items on the plate.
        """
        return super().count() + 1

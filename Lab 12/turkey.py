from plate_decorator import PlateDecorator

class Turkey(PlateDecorator):
    """Inherits the Plate Decorator class to decorate plate objects with a turkey."""
    
    def description(self) -> str:
        """The current contents of the plate with a turkey.

        Returns:
            str: The string that holds the plates description.
        """
        return super().description() + 'Turkey and '

    def area(self) -> int:
        """The area of the plate and its contents minus a turkey's area.

        Returns:
            int: The area the plate can hold.
        """
        return super().area() - 15

    def weight(self) -> int:
        """The weight of the plate and its contents minus a turkey's weight.

        Returns:
            int: The weight the plate can hold.
        """
        return super().weight() - 4

    def count(self) -> int:
        """The count of items on the plate.

        Returns:
            int: Number of items on the plate.
        """
        return super().count() + 1

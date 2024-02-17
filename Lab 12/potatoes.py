from plate_decorator import PlateDecorator

class Potatoes(PlateDecorator):
    """Inherits the Plate Decorator class to decorate plate objects with potatoes."""

    def description(self) -> str:
        """The current contents of the plate with potatoes.

        Returns:
            str: The string that holds the plates description.
        """
        return super().description() + 'Potatoes and '

    def area(self) -> int:
        """The area of the plate and its contents minus potatoe's area.

        Returns:
            int: The area the plate can hold.
        """
        return super().area() - 18

    def weight(self) -> int:
        """The weight of the plate and its contents minus potatoe's weight.

        Returns:
            int: The weight the plate can hold.
        """
        return super().weight() - 6

    def count(self) -> int:
        """The count of items on the plate.

        Returns:
            int: Number of items on the plate.
        """
        return super().count() + 1

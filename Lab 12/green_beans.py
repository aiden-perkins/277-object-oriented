from plate_decorator import PlateDecorator

class GreenBeans(PlateDecorator):
    """Inherits the Plate Decorator class to decorate plate objects with green beans."""

    def description(self) -> str:
        """The current contents of the plate with green beans.

        Returns:
            str: The string that holds the plates description.
        """
        return super().description() + 'Green Beans and '

    def area(self) -> int:
        """The area of the plate and its contents minus green bean's area.

        Returns:
            int: The area the plate can hold.
        """
        return super().area() - 20

    def weight(self) -> int:
        """The weight of the plate and its contents minus green bean's weight.

        Returns:
            int: The weight the plate can hold.
        """
        return super().weight() - 3

    def count(self) -> int:
        """The count of items on the plate.

        Returns:
            int: Number of items on the plate.
        """
        return super().count() + 1

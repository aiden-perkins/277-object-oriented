class Rectangle:
    """A class that holds a rectangles position and size.
    
    Attributes:
        w (int): The width of the rectangle.
        h (int): The height of the rectangle.
        x (int): The x coordinate of the rectangle.
        y (int): The y coordinate of the rectangle.
    """

    def __init__(self, w: int, h: int) -> None:
        """Initializes the rectangle object with the given width & height, and setting its position to (0, 0).

        Args:
            w (int): The width of the rectangle.
            h (int): The height of the rectangle.
        """
        self.w = w
        self.h = h
        self.x = 0
        self.y = 0
    
    def get_coords(self) -> tuple[int, int]:
        """
        Returns the x and y coordinates of the rectangle.
        
        Returns:
            tuple[int, int]: A length 2 tuple with the x & y coordinates.
        """
        return (self.x, self.y)
    
    def get_dimensions(self) -> tuple[int, int]:
        """
        Returns the dimensions of the rectangle.
        
        Returns:
            tuple[int, int]: A length 2 tuple with the width and height.
        """
        return (self.w, self.h)
    
    def move_up(self) -> None:
        """Decreases the x position by 1."""
        self.x -= 1
    
    def move_down(self) -> None:
        """Increases the x position by 1."""
        self.x += 1
    
    def move_left(self) -> None:
        """Decreases the y position by 1."""
        self.y -= 1
    
    def move_right(self) -> None:
        """Increases the y position by 1."""
        self.y += 1
    
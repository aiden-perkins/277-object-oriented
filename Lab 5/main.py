# Names: Aiden Perkins & Joshua Nwabuzor
# Date: September 18th, 2023
# Description: A program that asks the user for the width & height of a rectangle and asks them to move it on a grid.

import check_input
from rectangle import Rectangle

def display_grid(grid: list[list[str]]) -> None:
    """Prints out the given grid.

    Args:
        grid (list[list[str]]): A 20x20 2D list of strings.
    """
    print('\n'.join([''.join(x) for x in grid]))
    
def reset_grid(grid: list[list[str]]) -> None:
    """Resets the given grid to all periods.
    
    Args:
        grid (list[list[str]]): A 20x20 2D list of strings.
    """
    grid[:] = [['.' for _ in row] for row in grid]

def place_rect(grid: list[list[str]], rect: Rectangle) -> None:
    """Puts stars in the given grid where the given rectangle is.
    
    Args:
        grid (list[list[str]]): A 20x20 2D list of strings.
        rect (Rectangle): The rectangle object to place on the grid.
    """
    for i in range(rect.get_coords()[0], rect.get_dimensions()[1] + rect.get_coords()[0]):
        for j in range(rect.get_coords()[1], rect.get_dimensions()[0] + rect.get_coords()[1]):
            grid[i][j] = '*'

def main() -> None:
    """Asks the user to input a width and height and constantly asks them if they want to move it."""
    width = check_input.get_int_range('Enter rectangle width (1-5): ', 1, 5)
    height = check_input.get_int_range('Enter rectangle height (1-5): ', 1, 5)
    rect = Rectangle(width, height)
    grid = [dot[:] for dot in [['.'] * 20] * 20]
    option = 0
    while option != 5:
        place_rect(grid, rect)
        display_grid(grid)
        option = check_input.get_int_range('Enter Direction:\n1. Up\n2. Down\n3. Left\n4. Right\n5. Quit\n', 1, 5)
        if rect.get_coords()[1] > 0 and option == 3:
            rect.move_left()
        if rect.get_coords()[0] > 0 and option == 1:
            rect.move_up()
        if rect.get_coords()[1] + rect.get_dimensions()[0] < 20 and option == 4:
            rect.move_right()
        if rect.get_coords()[0] + rect.get_dimensions()[1] < 20 and option == 2:
            rect.move_down()
        reset_grid(grid)

if __name__ == '__main__':
    main()

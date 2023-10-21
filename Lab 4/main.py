# Names: Aiden Perkins & Joshua Nwabuzor
# Date: September 13th, 2023
# Description: Allows the user to enter instructions on how to move an X through a maze until they get to the 'f' position.

import check_input

def read_maze() -> list[list[str]]:
    """Reads contents from a text file and puts them into a 2D matrix of strings.
    
    Returns:
        list[list[str]]: A 2D matrix of strings.
    """
    return [list(a[:-1]) for a in open('maze-1.txt', 'r').readlines()]
    
def find_start(maze: list[list[str]]) -> list[int]:
    """Find the start position from the given maze.
    
    Args:
        maze (list[list[str]]): The maze that we want to find the start of, 2D matrix of strings.

    Returns:
        list[int]: A list of size 2 that holds the position of the starting point.
    """
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == 's':
                return [row, column]
    raise Exception('Invalid maze - no starting position')

def display_maze(maze: list[list[str]], loc: list[int]) -> None:
    """Prints out the maze with the given position as an X.

    Args:
        maze (list[list[str]]): The maze that we want to find the start of, 2D matrix of strings.
        loc (list[int]): The location that the player is currently at in the maze, size 2 int list.
    """
    temp = [row[:] for row in maze]
    temp[loc[0]][loc[1]] = 'X'
    print('\n'.join([''.join(x) for x in temp]))

def main() -> None:
    """Prompts the user to move through a maze and try and finish."""
    print('-Maze Solver-')
    maze = read_maze()
    loc = find_start(maze)
    while maze[loc[0]][loc[1]] != 'f':
        display_maze(maze, loc)
        direction = [[loc[0]-1, loc[1]], [loc[0]+1, loc[1]], [loc[0], loc[1]+1], [loc[0], loc[1]-1]]
        print('1. Go North\n2. Go South\n3. Go East\n4. Go West')
        option = direction[check_input.get_int_range('Enter choice: ', 1, 4) - 1]
        if maze[option[0]][option[1]] == '*':
            print('You cannot move there.')
            continue
        loc = option
    display_maze(maze, loc)
    print('Congratulations! You solved the maze.')

if __name__ == '__main__':
    main()

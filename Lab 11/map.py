class Map:
    """A Singleton class that represents the map of the dungeon maze.

    Class Attributes:
        _instance (Map) = The map that has been created, or None.
        _initialized (bool) = If a map has been created yet or not.

    Attributes:
        _map (lis[list[str]]): The contents of the file.
        _revealed (list[list[bool]]): Used to determine whether the contents of the map are displayed or not.
    """
    _instance: 'Map' = None
    _initialized: bool = False

    def __new__(cls) -> 'Map':
        """Creates a new map object from the class if one hasn't been created yet.

        Returns:
            Map: Either the newly created Map or the pre-existing Map object.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Fills the map list from the file contents. Creates and fills the revealed list with all False values."""
        if not Map._initialized:
            self.load_map(1)
            Map._initialized = True

    def load_map(self, map_num) -> None:
        self._map = [list(a.replace('\n', '')) for a in open(f'map{map_num}.txt', 'r').readlines()]
        self._revealed = [f[:] for f in [[False] * len(self._map)] * len(self._map)]
    
    def __getitem__(self, row: int) -> list[str]:
        """Returns the specified row from the map.

        Args:
            row (int): The index of the list of strings you want from _map.

        Returns:
            list[str]: The list of strings at index row of _map.
        """
        return self._map[row]

    def __len__(self) -> int:
        """Returns the number of rows in the map list.

        Returns:
            int: The number of rows in the map list.
        """
        return len(self._map)

    def show_map(self, loc: list[int]) -> str:
        """Returns the map as a string of characters where revealed locations are the characters from the map, unrevealed locations are 'x's, and the hero's location is a *.

        Args:
            loc (list[int]): The location of the hero.

        Returns:
            str: The string of characters that displays the map with specified characters.
        """
        s = ''
        for i, row in enumerate(self._map):
            t = ''
            for j, column in enumerate(row):
                if loc == [i, j]:
                    t += '*'
                elif self._revealed[i][j]:
                    t += column
                else:
                    t += 'X'
            s += t + '\n'
        return s

    def reveal(self, loc: list[int]) -> None:
        """Sets the value in the revealed list at the specified location to True.

        Args:
            loc (list[int]): The location to be set to True.
        """
        self._revealed[loc[0]][loc[1]] = True

    def remove_at_loc(self, loc: list[int]) -> None:
        """Overwrites the character in the map list at the specified location with an 'n'.

        Args:
            loc (list[int]): The location to be set to 'n'.
        """
        self._map[loc[0]][loc[1]] = 'n'


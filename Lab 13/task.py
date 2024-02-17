class Task:
    """A class that represents a task that holds important information.
    
    Attributes:
        desc (str): The description of the task.
        date (str): The date of the task in the format MM/DD/YYYY.
        time (str): The time of the task in the format HH:MM.
    """
    def __init__(self, desc: str, date: str, time: str) -> None:
        """Initializes the description, date, and time of the task.

        Args:
            desc (str): The description of the task.
            date (str): The date of the task in the format MM/DD/YYYY.
            time (str): The time of the task in the format HH:MM.
        """
        self._desc = desc
        self._date = date
        self._time = time

    @property
    def date(self):
        """Returns the date."""
        return self._date
    
    def __str__(self) -> str:
        """Summarizes the task object into a string to be printed.

        Returns:
            str: Returns a string that summarizes the task.
        """
        return f'{self._desc} - Due: {self._date} at {self._time}'

    def __repr__(self) -> str:
        """Combines the attributes of the task into a string to write to a file.

        Returns:
            str: All of the attributes combined with commas.
        """
        return ','.join([self._desc, self._date, self._time])

    def __lt__(self, a: 'Task') -> bool:
        """Compares 2 task objects to see which one has a closer date/time, order is year, month, day, hour, minute, then description.

        Args:
            a (Task): The task object being compared against.

        Returns:
            bool: If the current task object is less than the given task object.
        """
        return (self._date[-4:], self._date[:2], self._date[3:5], self._time, self._desc) < (a.date[-4:], a.date[:2], a.date[3:5], a._time, a._desc)
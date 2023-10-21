from task import Task

class TaskList:
    """A class to hold a list of task objects that the user has to complete.
    
    Attributes:
        tasklist (list[Task]): A list of the task objects to be completed.
    """
    def __init__(self) -> None:
        """Initializes the tasklist and reads from a file to populate it with tasks."""
        self.tasklist = []
        for line in open('tasklist.txt', 'r').readlines():
            self.add_task(*line.replace('\n', '').split(','))

    def add_task(self, desc: str, date: str, time: str) -> None:
        """Creates a task object from the given description, date, and time, and adds it to the list of tasks, then sorts the tasklist.

        Args:
            desc (str): The description of the task.
            date (str): The date of the task in the format MM/DD/YYYY.
            time (str): The time of the task in the format HH:MM.
        """
        self.tasklist.append(Task(desc, date, time))
        self.tasklist.sort()

    def mark_complete(self) -> Task:
        """Removes the first item in the task list and returns it to the user.

        Returns:
            Task: The completed task object.
        """
        return self.tasklist.pop(0)

    def save_file(self) -> None:
        """Saves all of the current tasks in the tasklist to a file."""
        open('tasklist.txt', 'w').writelines([repr(task) + '\n' for task in self.tasklist])

    def __getitem__(self, index: int) -> Task:
        """_summary_

        Args:
            index (int): The index of the task you want.

        Returns:
            Task: The task object at the specific index.
        """
        return self.tasklist[index]

    def __len__(self) -> int:
        """Returns the length of the tasklist.

        Returns:
            int: The length of the tasklist.
        """
        return len(self.tasklist)
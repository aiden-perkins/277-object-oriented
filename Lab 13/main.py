# Names: Aiden Perkins & Joshua Nwabuzor
# Date: , 2023
# Description: 
from tasklist import TaskList
import check_input

def main_menu() -> int:
    """Prints the menu and asks the user what they want to do.

    Returns:
        int: The option they choose between 1 & 6.
    """
    print('1. Display current task')
    print('2. Display all tasks')
    print('3. Mark current task complete')
    print('4. Add new task')
    print('5. Search by Date')
    print('6. Save and quit')
    return check_input.get_int_range('Enter choice: ', 1, 6)

def get_date() -> str:
    """Asks the user to enter a month, day, and year.

    Returns:
        str: The date in the format MM/DD/YYYY.
    """
    print('Enter due date:')
    month = str(check_input.get_int_range('Enter month: ', 1, 12)).zfill(2)
    day = str(check_input.get_int_range('Enter day: ', 1, 31)).zfill(2)
    year = str(check_input.get_int_range('Enter year: ', 2000, 3000))
    return f'{month}/{day}/{year}'

def get_time() -> str:
    """Asks the user to enter an hour & minute.

    Returns:
        str: The time in the format HH:MM.
    """
    print('Enter time:')
    hour = str(check_input.get_int_range('Enter hour: ', 0, 23)).zfill(2)
    minute = str(check_input.get_int_range('Enter minute: ', 0, 59)).zfill(2)
    return f'{hour}:{minute}'

def main() -> None:
    """Creates a tasklist object and continuously asks the user what they want to do and then performs that action."""
    tasklist = TaskList()
    option = 0
    while option != 6:
        print(f'-Tasklist-\nTasks to complete: {len(tasklist)}')
        option = main_menu()
        if len(tasklist) == 0 and option not in [4, 5]:
            print('All tasks complete.')
        elif option == 1:
            print(f'Current task is: \n{tasklist.get_current_task()}')
        elif option == 2:
            [print(a) for a in tasklist]
        elif option == 3:
            print(f'Marking current task as complete: {tasklist.mark_complete()}')
            if len(tasklist) != 0:
                print(f'New current task is: {tasklist.get_current_task()}')
            else:
                print('All tasks complete.')
        if option == 4:
            desc = input('Enter a task: ')
            tasklist.add_task(desc, get_date(), get_time())
        if option == 5:
            desired_date = get_date()
            for task in tasklist:
                if desired_date == task.date:
                    print(task)
        print()
    tasklist.save_file()

if __name__ == '__main__':
    main()

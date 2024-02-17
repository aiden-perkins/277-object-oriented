# Names: Aiden Perkins & Joshua Nwabuzor
# Date: December 4th, 2023
# Description: Puppy simulator program that has two basic functions: to feed or play with the puppy. The puppy will react differently to these functions based on which state it is currently in. The puppy has three possible states: asleep, eating, or playing.
import check_input
import puppy


def main() -> None:
    """Asks the user what they want to do with the puppy."""
    p = puppy.Puppy()
    answer = 0
    print('Congratulations on your new puppy!')
    while answer != 3:
        print('What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit')
        answer = check_input.get_int_range('Enter choice: ', 1 ,3)
        print()
        if answer == 1:
            print(p.give_food())
        elif answer == 2:
            print(p.throw_ball())
        

if __name__ == '__main__':
    main()

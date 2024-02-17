# Names: Aiden Perkins & Joshua Nwabuzor
# Date: November 13th, 2023
# Description: A game that has the user add food to their plate without going over the weight or area limit of a paper plate.
import check_input
from plate import Plate
from large_plate import LargePlate
from small_plate import SmallPlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie


def examine_plate(p: Plate) -> bool:
    """Displays the plate’s description, then based on the plate’s area and weight
    capacity remaining, displays a hint of how much more food the plate could hold.

    Args:
        p (Plate): The plate object to examine.

    Returns:
        bool: False if the plate has more area/weight, True otherwise.
    """
    print(p.description()[:-5])
    weight = p.weight()
    area = p.area()
    if weight < 1:
        print('Your plate isn\'t strong enough for this much food! Your plate tears in half.')
        return True
    if area < 1:
        print('Your plate isn\'t big enough for this much food! Your food spills over the edge.')
        return True
    print(f'Sturdiness: {["Bending", "Weak", "Strong"][min((weight - 1) // 6, 2)]}')
    print(f'Space available: {["Tiny bit", "Some", "Plenty"][min((area - 1) // 20, 2)]}')
    return False

def main() -> None:
    """Presents the user with a menu to choose the base plate type. Then repeatedly
    prompts the user to add a new food item to the plate, allowing the user to add food
    until they decide to quit, or they spill their food on the floor."""
    print('- Thanksgiving Dinner -')
    print('Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!')
    plate = [SmallPlate, LargePlate][check_input.get_int_range('Choose a plate\n1. Sturdy Small Plate\n2. Large Flimsy Plate\n', 1, 2) - 1]()
    plate_full = False
    while not plate_full:
        option = check_input.get_int_range('1. Turkey\n2. Stuffing\n3. Potatos\n4. Green Beans\n5. Pie\n6. Quit\n', 1, 6) - 1
        if option == 5:
            break
        plate = [Turkey, Stuffing, Potatoes, GreenBeans, Pie][option](plate)
        plate_full = examine_plate(plate)
    if not plate_full:
        print(plate.description()[:-5])
        print (f'Good job! You made it to the table with {plate.count()} items.')
        print(f'There was still {plate.area()} square inches left on your plate.')
        print(f'Your plate could have held {plate.weight()} more ounces of food.')
        print('Don\'t worry, you can always go back for more. Happy Thanksgiving!')
        

if __name__ == '__main__':
    main()

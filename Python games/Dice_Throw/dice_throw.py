import random


def print_dice(number):
    """Function prints a matching cube shape to a number."""
    match number:
        case 1:
            print("""
             _______
            |       |
            |   .   |
            |       |
            |_______|""")
        case 2:
            print("""
             _______
            | .     |
            |       |
            |     . |
            |_______|""")
        case 3:
            print("""
             _______
            | .     |
            |   .   |
            |     . |
            |_______|""")
        case 4:
            print("""
             _______
            | .   . |
            |       |
            | .   . |
            |_______|""")
        case 5:
            print("""
             _______
            | .   . |
            |   .   |
            | .   . |
            |_______|""")
        case 6:
            print("""
             _______
            | .   . |
            | .   . |
            | .   . |
            |_______|""")
        case _:
            print("""
             _______
            |       |
            |   .   |
            |       |
            |_______|""")


def dice_throw(how_many_times=1):
    """Gets random number and throw a dice.

    Args:
        how_many_times (int, optional): number of throws. Defaults to 1.
    """

    i = 0
    while i < how_many_times:
        i += 1
        throw = random.randint(1, 6)
        print_dice(throw)


print("\nHello at the dice throw!")

while True:
    print("""\nMenu:
    1 - throw a dice,
    2 - exit""")

    try:
        choice = int(input("\nYour choice: "))
    except ValueError:
        print("\nOnly numbers accepted.")
        continue

    if choice == 1:
        try:
            throw_number = int(
                input("\nPick how many time you want to throw a dice: "))
        except ValueError:
            print("\nOnly numbers accepted.")
            continue

        if throw_number <= 0:
            print("\nNumber has to be bigger than 0.")
        else:
            dice_throw(throw_number)
    elif choice == 2:
        break
    else:
        print("You have to pick 1 or 2.")

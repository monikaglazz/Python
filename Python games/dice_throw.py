import random


def one():
    print("""
     _______
    |       |
    |   .   |
    |       |
    |_______|""")


def two():
    print("""
     _______
    | .     |
    |       |
    |     . |
    |_______|""")


def three():
    print("""
     _______
    | .     |
    |   .   |
    |     . |
    |_______|""")


def four():
    print("""
     _______
    | .   . |
    |       |
    | .   . |
    |_______|""")


def five():
    print("""
     _______
    | .   . |
    |   .   |
    | .   . |
    |_______|""")


def six():
    print("""
     _______
    | .   . |
    | .   . |
    | .   . |
    |_______|""")


def dice_throw(how_many_times):
    i = 0
    while i < how_many_times:
        i += 1
        trow = random.randint(1, 6)
        if trow == 1:
            one()
        elif trow == 2:
            two()
        elif trow == 3:
            three()
        elif trow == 4:
            four()
        elif trow == 5:
            five()
        elif trow == 6:
            six()


print("\nHello at the dice throw!")

while True:
    print("""\nMenu:
    1 - throw a dice,
    2 - exit""")

    try:
        choice = int(input("\nYour choice: "))
    except ValueError:
        print("\nOnly numbers accepted.")

    if choice == 1:
        try:
            throw_number = int(
                input("\nPick how many time you want to throw a dice:"))
        except ValueError:
            print("\nOnly numbers accepted.")

        if throw_number <= 0:
            print("\nNumber has to be bigger than 0.")
        else:
            dice_throw(throw_number)
    elif choice == 2:
        break
    else:
        print("You have to pick 1 or 2.")

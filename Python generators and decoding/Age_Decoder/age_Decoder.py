from datetime import datetime


def calculate_age(age, yearNow):
    """Gets user age.

    Args:
        age (int): year of birth
        yearNow (_type_): current year

    Returns:
        int: user age
    """
    return yearNow - age


# Getting current year
yearNow = datetime.now().year

print("Hello! You can calculate how many years you have with me!")
while True:

    try:
        # Getting user year of birth
        userYear = int(input("\nYear of your birthday: "))

        # Lets check if somebody isn't from future
        if userYear <= yearNow:
            print("\nYour actual age:", calculate_age(userYear, yearNow))
            break
        else:
            print("\nWrong year! Are you from future? :)")
            continue
    except ValueError:
        print("\nWrong format! You have to gave full year e.g. 2001")
        continue

# A leap year (also known as an intercalary year or bissextile year) is a
# calendar year that contains an additional day added to keep the calendar
# year synchronized with the astronomical year or seasonal year. We have
# a leap year when a year can be divided by 4 but not by 100 or can
# be divided by 400.


def leap_year(year):
    """Check if given year is a leap year

    Args:
        year (int): year to check

    Returns:
        bool: True if is a leap year, False if not
    """

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


given_year = 0

while True:
    try:
        user_year = int(input("Give the year you want to check: "))
        given_year = user_year
    except ValueError:
        print("You can give only number, e.x. 1999.")

    is_it = leap_year(given_year)

    if is_it is True:
        print("The", given_year, "is a leap year.")
    else:
        print("The", given_year, "is not a leap year.")

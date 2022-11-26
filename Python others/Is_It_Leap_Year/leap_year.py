# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day
# added to keep the calendar year synchronized with the astronomical year or seasonal year. We have a leap year when
# a year can be divided by 4 but and not by 100 or can be divided by 400.


# Function is deciding if a given year is a leap year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


while True:
    try:
        user_year = int(input("Give the year you want to check: "))
    except ValueError:
        print("You can give only number, e.x. 1999.")

    is_it = leap_year(user_year)

    if is_it == True:
        print("The", user_year, "is a leap year.")
    else:
        print("The", user_year, "is not a leap year.")

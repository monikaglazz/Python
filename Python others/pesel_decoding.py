# (pol. Polski Powszechny Elektroniczny System Ewidencji Ludności) Universal Electronic System for Registration
# of the Population is the national identification number used in Poland since 1979. It always has 11 digits,
# identifies just one person and cannot be changed to another one (except some specific situations such as gender
# reassignment).


# check if pesel has all necessary elements
def check_if_pesel_is_correct(pesel):

    #  length is 11
    if len(pesel) == 11:

        # change str to list of digits
        pesel_list_digits = [int(x) for x in str(pesel)]

        # sum of numbers weight
        sum_number_weight = (1 * pesel_list_digits[0]+ 3* pesel_list_digits[1]
                             + 7 * pesel_list_digits[2] + 9 * pesel_list_digits[3]
                             + 1 * pesel_list_digits[4] + 3 * pesel_list_digits[5]
                             + 7 * pesel_list_digits[6] + 9 * pesel_list_digits[7]
                             + 1 * pesel_list_digits[8] + 3 * pesel_list_digits[9])

        # get the modulo of sum
        modulo = sum_number_weight % 10

        # get the last number from pesel
        last_number = pesel_list_digits[10]

        # check if pesel is correct
        if (10 - modulo) == last_number or modulo == last_number:
            return int(pesel)
        else:
            return 0

    # length is different
    else:
        return 0

# decode pesel information


def decode_date_of_birth_and_sex(pesel):

    pesel_str = str(pesel)

    # get the number that define the sex
    sexNumber = int(pesel_str[9])

    # decide which sex is it
    if sexNumber % 2 == 0:
        sex = "Women"
    else:
        sex = "Men"

    # get the year numbers
    year = int(pesel_str[:2])

    # get the month numbers
    month = int(pesel_str[2:4])

    # get the day numbers
    day = int(pesel_str[4:6])

    # change for correct date parameters
    if month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        year += 2000
        day -= 20
    elif 41 <= month <= 52:
        year += 2100
        day -= 40
    elif 61 <= month <= 72:
        year += 2200
        day -= 60
    elif 81 <= month <= 92:
        year += 1800
        day -= 80

    return [day, month, year, sex]


print("""\nHello at pesel decoding! Let's crack it.""")

# get data from user
pesel = input("\nInput PESEL number: ")

# check data
correct_pesel = check_if_pesel_is_correct(pesel)

# decode given data
if correct_pesel != 0:
    data = decode_date_of_birth_and_sex(correct_pesel)
    if data[1] < 10:
        print(
            f"\nDate of birth (yyyy - mm - dd): {data[2]} - 0{data[1]} - {data[0]}, Sex: {data[3]}")
    else:
        print(
            f"\nDate of birth (yyyy - mm - dd): {data[2]} - {data[1]} - {data[0]}, Sex: {data[3]}")
else:
    print("Your Pesel is incorrect. Try again")

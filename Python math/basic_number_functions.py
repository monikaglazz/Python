import math


# Function to calculate average of numbers
def average(*numbers):
    """Gets average of numbers.

    Returns:
        float: average of numbers
    """
    return sum(numbers) / len(numbers)


# Function to calculate geometric average of numbers
def geometric_average(*numbers):
    """Gets geometric average of numbers.

    Returns:
        float: average of numbers
    """
    return math.prod(numbers) ** (len(numbers) / 100)


# Function to find all dividers for a number
def dividers_for_number(number):
    """Gets all dividers for a number.

    Args:
        number (int): number for which we want dividers

    Returns:
        list: list of int
    """
    listOfDividers = list()
    for numberInRange in range(1, number + 1):
        if number % numberInRange == 0:
            listOfDividers.append(numberInRange)

    return listOfDividers


# Function to find less common multiply for two numbers
def less_common_multiply(first_number, second_number):
    """Gets the less common multiply for two numbers.

    Args:
        first_number (_type_): first number from pair
        second_number (_type_): second number from pair

    Returns:
        int: less common multiply
    """
    while True:
        if first_number < second_number:
            for number in range(first_number,
                                (first_number * second_number) + 1):
                if number % first_number == 0 and number % second_number == 0:
                    return number
        else:
            first = first_number
            first_number = second_number
            second_number = first
            continue


# Function to find greatest common divisor for two numbers
def greatest_common_divisor(first_number, second_number):
    """Gets the greatest common divisor for two numbers.

    Args:
        first_number (_type_): first number from pair
        second_number (_type_): second number from pair

    Returns:
        int: greatest common divisor
    """
    while True:
        if first_number < second_number:
            divisor = 1
            for number in range(1, first_number + 1):
                if first_number % number == 0 and second_number % number == 0:
                    divisor = number
            return divisor
        else:
            first = first_number
            first_number = second_number
            second_number = first
            continue


# Function to check if number is prime or not
def prime_number_test(number):
    """Check if number is prime or not.

    Args:
        number (int): number to check

    Returns:
        bool: True for prime, False for not.
    """
    dividers = 0
    for divider in range(2, number):
        if number % divider == 0:
            dividers += 1

    if dividers == 0:
        return True
    else:
        return False


print(average(3, 44, 30, 19, 78))

print(geometric_average(3, 44, 30, 19, 78))

print(dividers_for_number(48))

print(less_common_multiply(81, 35))

print(greatest_common_divisor(48, 45))

print(prime_number_test(45))

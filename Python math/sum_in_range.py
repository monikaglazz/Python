

# The role of function is to sum numbers in specific range
def sum_in_range(start=0, end=1):
    """Gets the sum of numbers in given range.

    Args:
        start (int, optional): start of range. Defaults to 0.
        end (int, optional): end of range. Defaults to 1.

    Returns:
        int: sum of numbers
    """
    sum = 0
    if start > end:
        for x in range(start, end, -1):
            sum += x
    else:
        for x in range(start, end + 1, 1):
            sum += x

    return sum


print(sum_in_range(0, 10))
print(sum_in_range(10, 0))

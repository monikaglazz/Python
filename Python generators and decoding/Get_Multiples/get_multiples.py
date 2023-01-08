# Write a function called get_multiples, which accepts a number and a count,
# and returns a generator that yields the first count multiples of the number.


def get_multiples(number=1, count=10):
    """Generator that yields the first count multiples of the number.

    Example behavior:
        evens = get_multiples(2, 3)
        next(evens) # 2
        next(evens) # 4
        next(evens) # 6
        next(evens) # StopIteration

        default_multiples = get_multiples()
        list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Args:
        number (int, optional): number to multiply. Defaults to 1.
        count (int, optional): count multiples of the number. Defaults to 10.

    Yields:
        int: multiplied number
    """
    x = 1
    while x <= count:
        yield number * x
        x += 1

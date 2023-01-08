def get_unlimited_multiples(number=1):
    """Generator that yields unlimited number of multiples of a number.

    Example behavior:
        sevens = get_unlimited_multiples(7)
        [next(sevens) for i in range(15)]
        # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

        ones = get_unlimited_multiples()
        [next(ones) for i in range(19)]
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    Args:
        number (int, optional): number to multiply. Defaults to 1.

    Yields:
        int: multiplied number
    """
    x = 1
    while True:
        yield number * x
        x += 1

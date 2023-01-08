def make_song(count=99, beverage='soda'):
    """Generator that yields verses from a popular song about a the beverage.

    Args:
        count (int, optional): number of verses in the song. Defaults to 99.
        beverage (str, optional): name of beverage. Defaults to 'soda'.

    Yields:
        str: number of bottles left
    """

    while count >= 0:
        if count == 0:
            yield "No more {}!".format(beverage)
        elif count == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "{} bottles of {} on the wall.".format(count, beverage)

        count -= 1

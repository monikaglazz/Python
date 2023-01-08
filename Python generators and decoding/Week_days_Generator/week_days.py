def week():
    """Generator that yields each day of the week starting from Monday.

    Yields:
        str: day of the week
    """

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                 'Friday', 'Saturday', 'Sunday']

    for day in week_days:
        yield day

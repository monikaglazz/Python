class Train:
    """
    Describe train.
    """

    def __init__(self, num_cars):
        """
        Args:
            num_cars (int): number of cars
        """
        self.num_cars = num_cars

    def __repr__(self):
        """
        Returns:
            str: describes the train
        """
        return "{0} car train".format(self.num_cars)

    def __len__(self):
        """
        Returns:
            int: length of train
        """
        return self.num_cars

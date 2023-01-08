class Mother:
    """
    Class with dominant traits
    """

    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


class Father:
    """
    Class with recessive traits
    """

    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    """
    Class inheriting from class Mother and class Father.

    Args:
        Mother (class): Class with dominant traits
        Father (class): Class with recessive traits
    """
    pass

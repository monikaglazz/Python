
class Character():
    """
    Describes properties of character.
    """

    def __init__(self, name, hp, level):
        """
        Args:
            name (str): name of character
            hp (int): value representing health (aka hit points)
            level (int): value representing experience level
        """
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    """
    Args:
        Character (class): parent class
    """

    def __init__(self, name, hp, level):
        """
        Args:
            name (str): name of character
            hp (int): value representing health (aka hit points)
            level (int): value representing experience level
        """
        super().__init__(name, hp, level)

    def speak(self):
        """Speech that character would say when a player interacts with them.

        Returns:
            str: speech of character
        """
        return "{0} says: 'I heard monsters!'".format(self.name)

from random import shuffle


class Card:
    """
    Describes the card elements.
    """

    def __init__(self, value, suit):
        """
        Args:
            value (str): value of card
            suit (str): suit of card
        """
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Returns:
            str: display the card's value and suit
        """
        return f"{self.value} of {self.suit}"


class Deck:
    """
    Describes the deck of cards.
    """

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        """
        Returns:
            str: deck of how many cards
        """
        return f"Deck of {self.count()} cards"

    def count(self):
        """Count of how many cards remain in the deck.

        Returns:
            int: how many cards remain
        """
        return len(self.cards)

    def _deal(self, num):
        """Accepts a number and removes at most that many cards from the deck.

        Args:
            num (int): number of cards to remove

        Raises:
            ValueError: if there are no cards left

        Returns:
            list: list of Cards
        """
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        """Deal a single card from the deck.

        Returns:
            list: list with a single Card
        """
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """Accepts a number and deal a list of cards from the deck.

        Args:
            hand_size (int): number of Cards to deal

        Returns:
            list: list with a hand of Cards
        """
        return self._deal(hand_size)

    def shuffle(self):
        """Shuffle a full deck of cards

        Raises:
            ValueError: if there are cards missing from the deck
        """
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()

# print(d.cards)

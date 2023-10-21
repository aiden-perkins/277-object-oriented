from card import Card
import random


class Deck:
    """A class to hold a list of cards and allow a card to be drawn and the deck to be shuffled.

    Attributes:
        _cards (list[Card]): A list of Card objects that are in the deck.
    """

    def __init__(self) -> None:
        """Initializes a standard deck of 52 cards. Thirteen ranks of each of the four suits."""
        self._cards = []
        for rank_i in range(13):
            for suit_i in range(4):
                self._cards.append(Card(suit_i, rank_i))

    def shuffle(self) -> None:
        """Shuffles the deck."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Removes the topmost card from the deck and returns it.

        Returns:
            Card: The card at the top.
        """
        return self._cards.pop(0)

    def __len__(self) -> int:
        """Returns the number of cards remaining in the deck.

        Returns:
            int: The cards remaining in the deck.
        """
        return len(self._cards)

from deck import Deck


class Player:
    """A class that represents a player in a blackjack game.

    Attributes:
        _hand (list[Card]): A list of Cards that the player is currently holding.
        _deck (Deck): A reference to the deck of cards that both the player and the dealer use.
    """

    def __init__(self, deck: Deck) -> None:
        """Sets the deck attribute, creates the player's hand, and gives the player 2 cards.

        Args:
            deck (Deck): A reference to the deck of cards that both the player and the dealer use.
        """
        self._deck = deck
        self._hand = []
        self.hit()
        self.hit()

    def hit(self) -> None:
        """Adds another card from the deck to the player’s hand and resorts them."""
        self._hand.append(self._deck.draw_card())
        self._hand.sort()

    def score(self) -> int:
        """Totals up the cards in the player’s hand and returns that score.

        Returns:
            int: The player's score.
        """
        _values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
        total = sum([_values[a.rank] for a in self._hand[:-1]])
        if total < 11 and self._hand[-1].rank == 12:
            total += 11
        else:
            total += _values[self._hand[-1].rank]
        return total

    def __str__(self) -> str:
        """Displays each of the cards in the player’s hand and the score of that hand.

        Returns:
            str: The player's cards and score as a string.
        """
        return '\n'.join(map(str, self._hand)) + '\nScore = ' + str(self.score())

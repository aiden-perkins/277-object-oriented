class Card:
    """A class that holds information about a playing card.

    Attributes:
        _suit (int): An integer index 0-3, representing the 4 card suits.
        _rank (int): An integer index 0-12, representing the 13 card ranks.
    """
    
    def __init__(self, suit: int, rank: int) -> None:
        """Initializes the suit and rank of the card.

        Args:
            suit (int): An integer index 0-3, representing the 4 card suits.
            rank (int): An integer index 0-12, representing the 13 card ranks.
        """
        self._suit = suit
        self._rank = rank

    def __str__(self) -> str:
        """Returns a string in the format ‘rank of suit’.

        Returns:
            str: The string that represents the card.
        """
        _ranks = ['2','3','4','5','6','7','8', '9', '10', 'Jack','Queen', 'King', 'Ace']
        _suits = ['Clubs', 'Diamonds','Hearts', 'Spades']
        return f'{_ranks[self._rank]} of {_suits[self._suit]}'

    def __lt__(self, other: 'Card') -> bool:
        """Compares the ranks of the self and other cards.

        Args:
            other (Card): The card we are comparing against.

        Returns:
            bool: Returns true if the self rank is less than the other rank.
        """
        return self._rank < other._rank

    @property
    def rank(self) -> int:
        """Get rank."""
        return self._rank
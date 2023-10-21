cofrom player import Player
from deck import Deck


class Dealer(Player):
    """Subclass for a player that represents the dealer and auto-plays."""

    def play(self) -> str:
        """Plays a round for the dealer
        
        Returns:
            str: What the dealer chose to do and their score.
        """
        s = ''
        while True:
            s += f'\nDealer\'s Cards:\n{str(self)}\n'
            if self.score() > 16:
                break
            s += 'Dealer Hits!\n'
            self.hit()
        return s

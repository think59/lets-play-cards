class Card:
    """
    Represents a single playing card with a rank and a suit.
    """

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, rank: str, suit: str):
        """
        Initialize a card with a specific rank (e.g., 'Ace') and suit (e.g., 'Hearts').
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Return a human-readable string representation of the card.
        Example: 'A of Hearts'
        """
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        """
        Return an unambiguous representation of the card, 
        useful for debugging or logging.
        """
        return f"Card({repr(self.rank)}, {repr(self.suit)})"

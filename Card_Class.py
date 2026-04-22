class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __add__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank
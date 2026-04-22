class Card:
    
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = self.get_value()
        
    def __add__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank
    
    def get_value(self):
        try:
            value = int(self.rank)
            return value
        except ValueError:  
            if(self.rank.lower() == "ace"):
                return 11
            return 10
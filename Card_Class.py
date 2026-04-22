class Card:
    
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = self.value_converter()
        
    def __add__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.get_value()+other.get_value()
    
    @value.setter
    def set_value(self, value):
        self.value = value
    
    def value_converter(self):
        try:
            value = int(self.rank)
            return value
        except ValueError:  
            if(self.rank.lower() == "ace"):
                return 11
            return 10
    
    def get_value(self):
        return self.value
class Card:
    """
    Represents a card in a game of Blackjack that can be held by other objects.
    
    Author: Michael
    """
        
    def __init__(self, rank: str, suit: str):
        """
        Initializes a card object.
        Create a new card with a rank, suit, and valuet.

        Args:
            rank (str): The rank of the card
            suit (int): The suit of the card

        Returns:
            None
        
        Author: Michael
        """
        self.rank = rank
        self.suit = suit
        self.value = self.value_converter()
        
    def __add__(self, other):
        """
        Dunder method override for adding two card objects

        Args:
            other (Card): the card to be added to the current card

        Returns:
            (int) the value of the 2 cards added together
        
        Author: Michael
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.get_value()+other.get_value()
    
    @value.setter
    def set_value(self, value):
        """
        Sets a card's value to the passed in value

        Args:
            value (int): value that you want to set the card to
            
        Returns:
            None
        
        Author: Michael
        """
        self.value = value
    
    def value_converter(self):
        """
        calculates a new card's value based off its rank
        
        Args:
            None
            
        Returns:
            None
        
        Author: Michael
        """
        try:
            value = int(self.rank)
            return value
        except ValueError:  
            if(self.rank.lower() == "ace"):
                return 11
            return 10
    
    def get_value(self) -> int:
        """
        returns a card's value

        Args:
            None
            
        Returns:
            this card's value attribute
        
        Author: Michael
        """
        return self.value
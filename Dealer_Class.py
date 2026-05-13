class Dealer:
    
    def __init__(self):
        """
        Purpose: Initialize a Dealer object with an empty hand
        
        Args:
            None

        Returns:
            None
        
        author: Sophia
        """
        self.hand = []
    
    def deal_to_self(self, deck):
        """
        Purpose: Deals one card from the deck and adds it to the dealer's hand
        
        Args:
            deck (Deck): The deck object used to deal cards

        Returns:
            None
            
        author: Sophia
        """
        card = deck.deal_card()
        self.hand.append(card)
    
    def show_hand(self, reveal_all=False):
        """
        Purpose: Returns the dealer's hand, optionally hiding the first card

        Args:
            reveal_all: If True, shows all cards in hand, if False, hides the first card

        Returns:
            A list of tuples representing cards in the hand, or a partially hidden representation
        
        author: sophia
        """
        if reveal_all:
            return [(card.rank, card.suit) for card in self.hand]
        else:
            if len(self.hand) > 1:
                return [("Hidden"), (self.hand[1].rank, self.hand[1].suit)]
            return []
    
    def get_hand_value(self):
        """
        Purpose: Calculates the total value of the dealer's hand,
             adjusting for Aces if needed

        Args:
            None

        Returns:
            Total value of the dealer's hand
                  
        author: Sophia
        """
        total = 0
        aces = 0
        
        for card in self.hand:
            total += card.get_value()
            if card.rank.lower() == "ace":
                aces += 1
        
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    
    def hand_description(self):
        """
        Purpose: returns a string description of the hand
        Arguments: none
        Returns: string representing information about the dealer's hand
        Author: Sophia
        """
        description = f"The house has {'an empty hand' if len(self.hand) == 0 else ''}"
        for card in self.hand:
            description+= f"{card} and "
        description = description[:-4] + f"\nThe total value is {self.get_hand_value()} points!\n"
        return description
    
    def play_turn(self, deck):
        """
        Purpose: Automates the dealer's turn by drawing cards until reaching 17 or higher

        Args:
            deck (Deck): The deck object used to deal cards

        Returns:
            None
            
        author: Sophia
        """
        while self.get_hand_value() < 17:
            self.deal_to_self(deck)
        
    def reset_hand(self):
        """
        Purpose: Clears the dealers hand for a new round

        Args:
            None

        Returns:
            None
            
        author: Sophia 
        """
        self.hand = []



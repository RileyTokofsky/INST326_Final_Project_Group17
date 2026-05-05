class Dealer:
    
    def __init__(self):
        """
        Purpose: Initialize a Dealer object with an empty hand
        
        author: Sophia
        """
        self.hand = []
    
    def deal_to_self(self, deck):
        """
        author: Sophia
        """
        card = deck.deal_card()
        self.hand.append(card)
    
    #I forgot to use this method.  Do y'all think we should use it instead?
    def show_hand(self, reveal_all=False):
        """
        author: Sophia
        """
        if reveal_all:
            return [(card.rank, card.suit) for card in self.hand]
        else:
            if len(self.hand) > 0:
                return [("Hidden"), (self.hand[1].rank, self.hand[1].suit)]
            return []
    
    def get_hand_value(self):
        """
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
        description = f"The house has a "
        for card in self.hand:
            description+= f"{card} and "
        description = description[:-4] + f"\nThe total value is {self.get_hand_value()} points!\n"
        return description
    
    def play_turn(self, deck):
        """
        author: Sophia
        """
        while self.get_hand_value() < 17:
            self.deal_to_self(deck)
        
    def reset_hand(self):
        self.hand = []



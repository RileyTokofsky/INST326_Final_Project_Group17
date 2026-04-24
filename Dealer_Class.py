class Dealer:
    
    def __init__(self):
        self.hand = []
    
    def deal_to_self(self, deck):
        card = deck.deal_card()
        self.hand.append(card)
    
    def show_hand(self, reveal_all=False):
        if reveal_all:
            return [(card.rank, card.suit) for card in self.hand]
        else:
            if len(self.hand) > 0:
                return [("Hidden", ""), (self.hand[1].rank, self.hand[1].suit)]
            return []
    
    def get_hand_value(self):
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
    
    def play_turn(self, deck):
        while self.get_hand_value() < 17:
            self.deal_to_self(deck)
    
    def reset_hand(self):
        self.hand = []



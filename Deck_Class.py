class Deck:
    
    def __init__(self, num_decks: int = 1):
        self.num_decks = num_decks
        self.cards = []
        self.percent_of_deck_used = 0.0
        self.build_deck()
        self.shuffle()
    
    def build_deck(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        
        for deck_num in range(self.num_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))
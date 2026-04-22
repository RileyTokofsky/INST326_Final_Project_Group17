class Deck:
    
    def __init__(self, num_decks: int = 1):
        self.num_decks = num_decks
        self.cards = []
        self.percent_of_deck_used = 0.0
        self.build_deck()
        self.shuffle()
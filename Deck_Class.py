import random

class Deck:
    """
    represents the decks of cards used in blackjack

    dne by: Riley Tokofsky
    """
    
    def __init__(self, num_decks: int = 6):
        """
        initializes the deck of cards
        Args:
            num_decks (int): number of decks to being used. Defualt amount is 6

        done by: Riley Tokofsky
        """
        self.num_decks = num_decks
        self.cards = []
        self.percent_of_deck_used = 0.0
        self.build_deck()
        self.shuffle()
    
    def build_deck(self):
        """
    creates the full deck of cards based on the number of decks

        Done by: Riley Tokofsky
        """
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for deck_num in range(self.num_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))
                    
    def shuffle(self):
        """
        shuffles the deck of cards

        done by: Riley Tokofsky
        Technique: N/A
        """
        random.shuffle(self.cards)
 
    def deal_card(self):
        """
        removes and returns the first card from the deck

        returns:
            card: card that was dealt

        done by: Riley Tokofsky
        Technique: N/A
        """
        if len(self.cards) == 0:
            raise ValueError("No cards left in deck")
        card = self.cards.pop()
        self.update_percent_used()
        return card

    def cards_left_in_deck(self):
        """
        returns the number of cards still in deck
        Returns:
            int: number of cards left

        done by: Riley Tokofsky
        """
        return len(self.cards)

    def update_percent_used(self):
        """
        the percentage of the deck used gets updated

        done by: Riley Tokofsky
        """
        total_cards = 52 * self.num_decks
        used_cards = total_cards - len(self.cards)
        self.percent_of_deck_used = used_cards / total_cards
class Player:
    """
    Represents the player in a game of Blackjack who must bet.
    
    Author: Adikari
    """
    def __init__(self, name, wallet):
        """
        Initializes a Player object.
        Create a new player with a name, empty hand, and starting wallet.

        Args:
            name (str): The name of the player
            wallet (int): Starting money amount

        Returns:
            None
        
        Author: Adikari
        """
        self.name = name
        self.wallet = wallet
        self.hand = []
        self.bets = []
    
    def place_bet(self, amount):
        """
        Places a bet for the player.
        Deducts money from the player's wallet and records the bet.

        Args:
            amount (int): The amount to bet

        Returns:
            True if bet is successful, False otherwise
        
        Author: Adikari
        """
        if amount > self.wallet:
            return False
        self.wallet -= amount
        self.bets.append(amount)
        return True
    
    def hit(self, deck):
        """
        Adds a card to the player's hand.

        Args:
            deck (Deck): The deck object

        Returns:
            None
        
        Author: Adikari
        """
        card = deck.deal_card()
        self.hand.append(card)
    
    def stand(self):
        """
        Ends the player's turn.

        Args:
            None

        Returns:
            None
        
        Author: Adikari
        """
        pass
    
    def split(self, deck):
        """
        Splitting a hand.

        Args:
            deck (Deck): Deck object

        Returns:
            None
        
        Author: Adikari
        """
        #1 Check if player has two cards
        #2 Check if both cards are the same rank
        #3 Check if player has enough money to split
        #4 Create two new hands
        #5 Deal one new card to each hand
        #6 Return or store the new hands
        pass
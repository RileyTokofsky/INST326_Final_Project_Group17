from Bet import StandardBet
from Dealer_Class import Dealer


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
        #might need to later implement having multiple hands for splitting
        self.hand = []
        self.bets = []
    
    def place_bet(self, amount):
        """
        Places a bet for the player.

        Args:
            amount (int): The amount to bet

        Returns:
            True if bet is successful, False otherwise
        
        Author: Adikari
        """
        if amount > self.wallet:
            return False
        self.wallet -= amount
        self.bets.append(StandardBet(amount))
        return True
    
    def get_hand_value(self, hand):
        total = 0
        aces = 0
        
        for card in hand:
            total += card.get_value()
            if card.rank.lower() == "ace":
                aces += 1
        
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    
    def hand_description(self, hand):
        description = f"{self.name} has a "
        for card in hand:
            description+= f"{card} and "
            description = description[:-4] + f"\nThe total value is {self.get_hand_value()} points!\n"
        return description
    
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
    
    def split(self, hand):
        """
        Splitting a hand.

        Args:
            None

        Returns:
            None
        
        Author: Adikari
        """
        if(len(self.hand) == 2):
            if self.hand[0].get_value() == self.hand[1].get_value():
                if(self):
                    #Code to test if you have enough money in your wallet to
                    #support 2 bets of the predetermined bet size
                    pass
                else:
                    print("You don't have enough money in your wallet to split")
            else:
                print("Your cards need to have the same rank to split")
        else:
            print("splitting failed, you need 2 cards in your hand exactly to split")
        #1 Check if player has two cards
        #2 Check if both cards are the same rank
        #3 Check if player has enough money to split
        #4 Create two new hands
        #5 Deal one new card to each hand
        #6 Return or store the new hands
        pass
    
    def double_down(self, hand):
        
        pass
    
    def insure(self, hand):
        pass
    
    def decide(self, arg_hand, dealer: Dealer) -> str:
        if self.get_hand_value(arg_hand) > 21:
            return "bust"
    #21 point tie rules
        elif (self.get_hand_value(arg_hand) == 21 and len(arg_hand) == 2
            and dealer.get_hand_value() == 21 and len(dealer.hand) == 2):
            return "push"
        elif (self.get_hand_value(arg_hand) == 21 and len(arg_hand) != 2
            and dealer.get_hand_value() == 21 and len(dealer.hand)!= 2):
            return "push"
        elif (self.get_hand_value(arg_hand) == 21 and len(arg_hand) == 2
            and dealer.get_hand_value() == 21 and len(dealer.hand) != 2):
            return "win"
        elif (self.get_hand_value(arg_hand) == 21 and len(arg_hand) != 2
            and dealer.get_hand_value() == 21 and len(dealer.hand)== 2):
            return "loss"
    #Other rules
        elif self.get_hand_value(arg_hand) < 21 and dealer.get_hand_value() > 21:
            return "win"
        elif self.get_hand_value(arg_hand) < dealer.get_hand_value():
            return "loss"
        elif self.get_hand_value(arg_hand) > dealer.get_hand_value():
            return "win"
        elif self.get_hand_value(arg_hand) == dealer.get_hand_value():
            return "push"
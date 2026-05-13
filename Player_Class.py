from Bet import Pairs, StandardBet
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
        self.hand = []
        self.bets = []
        self.insurance_bet = None
    
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
    
    def place_pair_bet(self, amount, type):
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
        self.bets.append(Pairs(amount, type))
        return True
    
    def get_hand_value(self, hand):
        """
        Purpose: returns the value a player's hand
        Arguments: hand as a list of cards
        Returns: total value of the hand
        Author: Ama
        """
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
        """
        Purpose: returns a string description of the hand
        Arguments: hand as a list of cards
        Returns: string representing information about the player and their hand
        Author: Ama
        """
        description = f"{self.name} has a "
        for card in hand:
            description+= f"{card} and "
        description = description[:-4] + f"\nThe total value is {self.get_hand_value(hand)} points!\n"
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
    
    
    def double_down(self, bet):
        """
        Purpose: doubles the value of a player's bet, "doubling down"
        Arguments: standard bet that you want to double down
        Returns: none
        Authors: Ama, Adikari
        """
        if len(self.hand) != 2:
            return False

        if bet is None:
            return False

        if self.wallet < bet.value:
            return False

        self.wallet -= bet.value
        bet.value *= 2

        return True
        
    
    def insure(self, amount):
        """
        Places an insurance bet.

        Args:
        amount (int): insurance amount

        Returns:
        bool

        Author: Adikari
        """
        if amount > self.wallet:
            return False

        self.wallet -= amount
        self.insurance_bet = StandardBet(amount)
        return True
    
    def resolve_insurance(self, dealer_has_blackjack):
        """
        Resolves insurance bet after dealer reveal.
        
        Args:
            dealer_has_blackjack: Whether dealer has blackjack

        Returns:
            None

        Author: Adikari
        """
        if self.insurance_bet is None:
            return

        if dealer_has_blackjack:
            self.insurance_bet.resolve("win")
        else:
            self.insurance_bet.resolve("loss")

        self.wallet += self.insurance_bet.payout()
        self.insurance_bet = None
        
    def decide(self, arg_hand, dealer: Dealer) -> str:
        """
        Purpose: decides the outcome of a player's standard bet
        Arguments: arg_hand as a hand you want to decide the outcome of,
            dealer that you're comparing your hand to
        Returns: string representing the outcome of your bet
        Authors: Ama, Adikari
        """
        player_value = self.get_hand_value(arg_hand)
        status = "bust" if player_value > 21 else "continue"
        if status == "bust":
            return "bust"
    #21 point tie rules
        elif (player_value == 21 and len(arg_hand) == 2
            and dealer.get_hand_value() == 21 and len(dealer.hand) == 2):
            return "push"
        elif (player_value == 21 and len(arg_hand) != 2
            and dealer.get_hand_value() == 21 and len(dealer.hand) != 2):
            return "push"
        elif (player_value == 21 and len(arg_hand) == 2
            and dealer.get_hand_value() == 21 and len(dealer.hand) != 2):
            return "blackjack"
        elif (player_value == 21 and len(arg_hand) != 2
            and dealer.get_hand_value() == 21 and len(dealer.hand) == 2):
            return "loss"
    #Other rules
        elif (player_value == 21 and len(arg_hand) == 2
            and dealer.get_hand_value() != 21):
            return "blackjack"
        elif player_value < 21 and dealer.get_hand_value() > 21:
            return "win"
        elif player_value < dealer.get_hand_value():
            return "loss"
        elif player_value > dealer.get_hand_value():
            return "win"
        elif player_value == dealer.get_hand_value():
            return "push"
        
    def decidePair(self, arg_hand, type) -> str:
        """
        Purpose: decides the outcome of a player's pair bet
        Arguments: arg_hand (list of cards), type (str) = pp, mp, cp
        Returns: "win" or "lose"
        Authors: Ama, Adikari
        """
        if len(arg_hand) < 2:
            return "lose"

        card1 = arg_hand[0]
        card2 = arg_hand[1]

        same_rank = card1.rank == card2.rank

        if not same_rank:
            return "lose"

        if type == "pp":
            if card1.suit == card2.suit:
                return "win"
            return "lose"

        elif type == "cp":
            red_suits = {"Hearts", "Diamonds"}
            black_suits = {"Spades", "Clubs"}

            if (
                (card1.suit in red_suits and card2.suit in red_suits)
                or (card1.suit in black_suits and card2.suit in black_suits)
            ):
                return "win"
            return "lose"

        elif type == "mp":
            return "win"

        return "lose"
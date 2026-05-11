#---------------------------WORKFLOW-------------------------------------------
from Dealer_Class import Dealer
from Deck_Class import Deck
from Player_Class import Player

"""
Purpose: plays the blackjack game
Arguments: none
Returns: none
Author: Ama
"""
def main():
#Ask how many players are playing using input()
#   error handling later
    people = int(input("how many players are playing today?\n"))
    num = 0
    players = []
#Loop up to number of players to create player objects
    #error handling later
    while num < people:
        response = input("tell us your name and how much money you brought to"
                         " the table in the format of [name,money]\n")
        response = response.split(",")
        players.append(Player(response[0].lower().strip(" "), int(response[1].strip(" "))))
        num+=1
#Start loop for game until each player says end when asked to bet
    #error handling with not enough money
    print("We'll now start betting\n")
    dealer = Dealer()
    deck = Deck()
    while len(players) > 0:
        dealer.hand = []
        for player in players:
            player.hand = []
            player.bets = []
            wager = input(f"{player.name}, you have ${player.wallet}.  "
                          "How much money do you want to bet?\n")
            player.place_bet(int(wager))
#everyone must bet
    #Ask for optional pre bet
        for player in players:
#dealer deals everyone 2 cards
    #error handling
            response = input("Any sidebets?"
            "  Respond with [pp] for Perfect Pairs or [mp] for Mixed Pairs or [cp] for Colored Pairs\n")
            if response.lower()=="pp":
                value = int(input("how much?\n"))
                player.place_pair_bet(value, "pp")
                
            elif response.lower() == "mp":
                value = int(input("how much?\n"))
                player.place_pair_bet(value, "mp")
                
            elif response.lower() == "cp":
                value = int(input("how much?\n"))
                player.place_pair_bet(value, "cp")
                
            player.hand.append(deck.deal_card())
            player.hand.append(deck.deal_card())
            print(f"\n\n{player.hand_description(player.hand)}")
#dealer deals himself 1 card
        dealer.deal_to_self(deck)
        print(f"The dealer has a {dealer.hand[0]}\n")
#Dealer asks each player to hit or stand, looping until they say stand or bust
    #error handling later
    #splitting later
    #insurance later
        for player in players:
            if player.get_hand_value(player.hand) == 21:
                print("Blackjack!\n")
            else:
                response = ""
                while player.get_hand_value(player.hand) < 21 and response.lower() != "stand" and response.lower() != "double down":
                    print(player.hand_description(player.hand))
                    response = input(f"{player.name}, do you want to hit, stand, or double down?"
                                    "  Respond with [hit] or [stand] or [double down]\n")
                    if response.lower()=="hit":
                        player.hit(deck)
                    elif response.lower() == "double down":
                        player.hit(deck)
                        player.double_down(player.bets[0])
                        print("you doubled your bet size!\n")
                    elif player.get_hand_value(player.hand) == 21:
                        print("You got 21, your turn is over\n")
                    elif player.get_hand_value(player.hand) > 21:
                        print("You busted\n")
            print(f"Final hand: {player.hand_description(player.hand)}\n")    
#dealer deals themself cards until total value >=17
        dealer.play_turn(deck)
        print(f"{dealer.hand_description()}\n")
#Dealer compares their hand to players and decides who wins and side bets
    #Side Bet implementation
        for player in players:
            if len(player.bets) >1:
                bet2 = player.bets[1]
                bet2.resolve(player.decidePair(player.hand, bet2.type))
                player.wallet += bet2.payout()
                if bet2.payout() != 0:
                    print("Your Pair bet won!\n")
                else:
                    print("Your Pair bet lost\n")
            
            bet = player.bets[0]
            bet.resolve(player.decide(player.hand, dealer))
            print(f"{player.name} got a {bet.result}!  Your old balance was "
                  f"{player.wallet + bet.value}.  Your new balance is "
                  f"{player.wallet + bet.payout()}\n")
            player.wallet += bet.payout()
#Ask which players want to keep playing
        for player in players[:]:
            response = input(f"{player.name}, "
                             "do you want to keep playing? Yes or No\n").lower()
            if response == "no":
                players = [one for one in players if one.name != player.name]
#Thank you
    print("Thank You for playing!")
    
if __name__ == "__main__":
    main()
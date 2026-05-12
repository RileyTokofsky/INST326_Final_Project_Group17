#---------------------------WORKFLOW-------------------------------------------
from Dealer_Class import Dealer
from Deck_Class import Deck
from Player_Class import Player

"""
Purpose: plays the blackjack game
Arguments: none
Returns: none
Authors: Ama, Adikari
"""
def main():
#Ask how many players are playing using input()
#   error handling later
    people = 0

    while people <= 0:

        try:
            people = int(input("how many players are playing today?\n"))

            if people <= 0:
                print("Please enter a valid number.\n")
                
            if people >= 8:
                print("There are only 8 seats at the table.\n")

        except ValueError:
            print("Please enter a valid integer.\n")

    players = []
#Loop up to number of players to create player objects
    #error handling later
    for _ in range(people):
        while True:
            try:
                response = input("tell us your name and money [name,money]\n")
                response = response.split(",")

                name = response[0].strip().lower()
                money = int(response[1].strip())

                players.append(Player(name, money))
                break

            except:
                print("Invalid format. Try again.")
#Start loop for game until each player says end when asked to bet
    #error handling with not enough money
    print("We'll now start betting\n")
    dealer = Dealer()

    while len(players) > 0:

        # reshuffle deck between rounds
        deck = Deck()

        dealer.hand = []
        for player in players:
            player.hand = []
            player.bets = []
            wager = 0

            while wager <= 0 or wager > player.wallet:

                try:
                    wager = int(input(f"{player.name}, you have ${player.wallet}.  "
                          "How much money do you want to bet?\n"))

                    if wager > player.wallet:
                        print("You cannot bet more than your wallet.\n")

                    elif wager <= 0:
                        print("Bet must be greater than 0.\n")

                except ValueError:
                    print("Please enter a valid integer.\n")

            player.place_bet(wager)
#everyone must bet
    #Ask for optional pre bet
        for player in players:
#dealer deals everyone 2 cards
    #error handling
            response = input("Any sidebets?"
            "  Respond with [pp] for Perfect Pairs or [mp] for Mixed Pairs or [cp] for Colored Pairs\n").lower()
            if response == "pp":
                value = int(input("how much?\n"))
                player.place_pair_bet(value, "pp")

            elif response == "mp":
                value = int(input("how much?\n"))
                player.place_pair_bet(value, "mp")

            elif response == "cp":
                value = int(input("how much?\n"))
                player.place_pair_bet(value, "cp")
                
            player.hand.append(deck.deal_card())
            player.hand.append(deck.deal_card())
            print(f"\n\n{player.hand_description(player.hand)}")
#dealer deals himself 1 card
        dealer.deal_to_self(deck)
        print(f"The dealer has a {dealer.hand[0]}\n")

# Insurance
        if dealer.hand and dealer.hand[0].rank.lower() == "ace":

            for player in players:

                if not player.bets:
                    continue

                response = input(f"{player.name}, do you want insurance? (yes/no)\n").lower()

                if response != "yes":
                    continue

                try:
                    amount = int(input("How much insurance?\n"))

                    if amount <= 0:
                        print("Insurance must be greater than 0.")
                        continue

                    max_insurance = player.bets[0].value / 2

                    if amount > max_insurance:
                        print("Insurance cannot exceed half your main bet.")
                        continue

                    if player.insure(amount):
                        print("Insurance placed.\n")
                    else:
                        print("Not enough money.\n")

                except ValueError:
                    print("Invalid insurance amount.\n")
      
#Dealer asks each player to hit or stand, looping until they say stand or bust
        for player in players:
            if player.get_hand_value(player.hand) == 21:
                print("Blackjack!\n")
            else:
                response = ""
                while player.get_hand_value(player.hand) < 21 and response.lower() != "stand" and response.lower() != "double down":
                    print(player.hand_description(player.hand))
                    response = ""
                    while response != "hit" and response != "stand" and response != "double down":
                        response = input(f"{player.name}, do you want to hit, stand, or double down?"
                     "  Respond with [hit] or [stand] or [double down]\n").lower()

                        if response != "hit" and response != "stand" and response != "double down":
                            print("Invalid response.\n")
                    if response.lower()=="hit":
                        player.hit(deck)
                    elif response.lower() == "double down":
                        player.hit(deck)
                        if player.bets:
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

# Insurance resolution 
        dealer_blackjack = (
            dealer.get_hand_value() == 21 and len(dealer.hand) == 2
        )

        for player in players:
            player.resolve_insurance(dealer_blackjack)
            
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
            response = ""

            while response != "yes" and response != "no":
                response = input(f"{player.name}, do you want to keep playing? Yes or No\n").lower()

                if response != "yes" and response != "no":
                    print("Please respond with Yes or No.\n")

            if response == "no":
                players = [one for one in players if one.name != player.name]
#Thank you
    print("Thank You for playing!")
    
if __name__ == "__main__":
    main()
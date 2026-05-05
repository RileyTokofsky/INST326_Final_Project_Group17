#---------------------------WORKFLOW-------------------------------------------
def main(self):
#Ask how many players are playing using input()
#   error handling later
    people = input("how many player are playing today?\n")
    num = 0
    players = {}
#Loop up to number of players to create player objects
    #error handling later
    while num < people:
        response = input("tell us your name and how much money you brought to"
                         " the table in the format of [name,money]\n")
        response = response.split(",")
        players[response[0].lower()] = Player(response[0].lower(), int(response[1]))
        num+=1
#Start loop for game until each player says end when asked to bet
    print("We'll now start betting\n")
    dealer = Dealer()
    deck = Deck()
    while players > 0:
#everyone must bet
        #Ask for optional pre bet
        for player in players:
#dealer deals everyone 2 cards
            player.hand.append(deck.deal_card())
            player.hand.append(deck.deal_card())
            print(player.hand_description(player.hand))
#dealer deals himself 1 card
        dealer.deal_to__self(deck)
        print(f"The dealer has a {dealer.hand[0]}")
#Dealer asks each player to hit or stand, looping until they say stand or bust
    #error handling later
    #splitting later
    #insurance later
        for player in players:
            if player.get_hand_value() == 21:
                print("Blackjack!")
            else:
                response = ""
                while player.get_hand_value <=21 or response.lower() == "stand":
                    print(player.hand_description(player.hand))
                    response = input(f"{player.name}, do you want to hit or stand?"
                                    "  Respond with [hit] or [stand]\n")
                    if response.lower=="hit":
                        player.hand.append(deck.deal_card())
                    if player.get_hand_value() == 21:
                        print("You got 21, your turn is over")
                    elif player.get_hand_value() > 21:
                        print("You busted")
            
                print(f"Final hand: {player.hand_description(player.hand)}")
                
                
                
#dealer deals themself cards until total value >=17
#Dealer compares their hand to players and decides who wins and side bets
#Betting loop starts again
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
            print(f"{player.name} has a ")
            description = ""
            points = 0
            for card in player.hand():
                description+= f"{card} and "
                points += card.get_value()
            print(description[:-4] + f"\nThe total value is {points} points!\n")
#dealer deals himself 1 card
        dealer.deal_to__self(deck)
        print(f"The dealer has a {dealer.hand[0]}")
#Dealer asks each player to hit or stand, looping until they say stand or bust
    #error handling later
    #splitting later
    #insurance later
        for player in players:
            response = input(f"{player.name}, do you want to hit or stand?"
                             "  Respond with [hit] or [stand]\n")
            if response.lower=="hit":
                player.hand.append(deck.deal_card)
            elif response.lower()=="stand":
                
#dealer deals themself cards until total value >=17
#Dealer compares their hand to players and decides who wins and side bets
#Betting loop starts again
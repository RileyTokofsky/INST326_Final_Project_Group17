#---------------------------WORKFLOW-------------------------------------------
from Dealer_Class import Dealer
from Deck_Class import Deck
from Player_Class import Player


def main():
#Ask how many players are playing using input()
#   error handling later
    people = int(input("how many player are playing today?\n"))
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
        for player in players:
            wager = input(f"{player.name}, you have ${player.wallet}.  "
                          "How much money do you want to bet?\n")
            player.place_bet(int(wager))
            player.wallet -= int(wager)
#everyone must bet
    #Ask for optional pre bet
        for player in players:
#dealer deals everyone 2 cards
            player.hand.append(deck.deal_card())
            player.hand.append(deck.deal_card())
            print(player.hand_description(player.hand))
#dealer deals himself 1 card
        dealer.deal_to__self(deck)
        print(f"The dealer has a {dealer.hand[0]}\n")
#Dealer asks each player to hit or stand, looping until they say stand or bust
    #error handling later
    #splitting later
    #insurance later
        for player in players:
            if player.get_hand_value() == 21:
                print("Blackjack!\n")
            else:
                response = ""
                while player.get_hand_value <=21 or response.lower() == "stand":
                    print(player.hand_description(player.hand))
                    response = input(f"{player.name}, do you want to hit or stand?"
                                    "  Respond with [hit] or [stand]\n")
                    if response.lower=="hit":
                        player.hit(deck)
                    if player.get_hand_value() == 21:
                        print("You got 21, your turn is over\n")
                    elif player.get_hand_value() > 21:
                        print("You busted\n")
            print(f"Final hand: {player.hand_description(player.hand)}\n")    
#dealer deals themself cards until total value >=17
        dealer.play_turn(deck)
        print(f"{dealer.hand_description()}\n")
#Dealer compares their hand to players and decides who wins and side bets
    #Side Bet implementation
        for player in players:
            bet = player.bets[0]
            bet.resolve(player.decide(player.hand, dealer))
            print(f"{player.name} got a {bet.result}!  Your old balance was "
                  f"{player.wallet+bet.value}.  Your new balance is "
                  f"{player.wallet+bet.payout()}\n")
            player.wallet+=bet.payout()
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
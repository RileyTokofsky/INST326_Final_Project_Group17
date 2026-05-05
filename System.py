#---------------------------WORKFLOW-------------------------------------------
def main(self):
#Ask how many players are playing using input()
#   error handling later
    people = input("how many player are playing today?")
    num = 0
    players = 
#Loop up to number of players to create player objects
    while num < people:
        response = input("tell us your name and how much money you brought to the table")
        
#Start loop for game until each player says end when asked to bet
#everyone must bet
#   Ask for optional pre bet
#dealer deals everyone 2 cards
#dealer deals himself 1 card
#Dealer asks each player to hit or stand, looping until they say stand
#dealer deals themself cards until total value >=17
#Dealer compares their hand to players and decides who wins and side bets
#Betting loop starts again
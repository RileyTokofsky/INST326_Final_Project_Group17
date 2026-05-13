Blackjack is a card game where the player tries to reach 21—or as close as possible—without going over, while competing against a dealer. Because the next card is unknown, the player must rely on judgment and chance to decide their moves. The game is commonly associated with gambling and winning money.

Players can take several actions: “hit” (take another card), “stand” (end their turn), “double down” (double their bet after the first two cards), and optional bets like insurance or Perfect Pairs. Each round starts with both the player and dealer receiving initial cards. The player then chooses actions until they stand or bust, while the dealer follows similar play. Rounds repeat until the player decides to stop.


Purpose of each file:
Card_Class: Defines a single playing card used in the game. Each card has a suit (Hearts, Diamonds, Clubs, Spades) and a rank/value. This class provides the basic building block for the deck system and is used throughout the program whenever cards are created, displayed, or evaluated for hand values.

Dealer_Class: Represents the dealer in the Blackjack game. The dealer interacts with the Deck_Class to draw cards and manages the dealer’s hand according to Blackjack rules. This class is responsible for automating dealer behavior during each round.

Deck_Class: Represents one or more shuffled decks of standard playing cards. This class is responsible for creating a full set of Card objects, shuffling them, and managing which cards have already been dealt. It provides functionality for drawing cards during gameplay and removes cards from the deck once used.

Player_Class: Represents the player in the game. This class manages the player’s hand, betting actions, and decisions such as hit or stand. It also calculates the player’s score and determines whether the player has won, lost, or busted during a round.


Instructions:
To run the Blackjack program, make sure all of the files are in the same folder. This includes the Bet.py, Card_Class.py, Dealer_Class.py, Deck_Class.py, Player_Class.py, and the System.py. Open a command prompt and navigate to the project folder. To run the program you can type python System.py. The game will then start in the terminal window.

How to use: 
When the game begins the program asks how many players are playing. Each player enters their name and money. Players place bets at the start of each round and also choose their side bets. After the cards are dealt, players can choose to hit, stand, or double down. The program shows each player's cards and total hand value during the round. If a players total goes over 21 points they bust. After all players finish their turns the dealer plays and bets are resolved then players can choose whether to continue playing or end the game.

All input is entered through the terminal using the keyboard. There are no buttons or graphical interface elements. When prompted for bets or decisions, users must enter valid inputs exactly as shown below:
Side bets must be entered as:
pp = Perfect Pairs
mp = Mixed Pairs
cp = Colored Pairs
Any other input is treated as invalid and the side bet will not be placed.

For main gameplay decisions, players must type:
hit to receive another card
stand to end their turn
double down to double their bet and take one final card

If a player enters an invalid response, the program will prompt them again until a valid input is provided. If a player chooses not to place a side bet, they can simply press Enter or type anything other than pp, mp, or cp. The game runs entirely in the command-line terminal and does not require any external windows or interfaces.

Annotated bibliography:
This source was used to understand the official rules of Blackjack, including player actions such as hit, stand, and double down. It helped guide the logic implemented in the Player and Dealer classes: 
Bicycle. (2025). Blackjack. Bicyclecards.com. https://bicyclecards.com/how-to-play/blackjack

This source helped with understanding how to structure classes in Python, which was needed for implementing the Card, Deck, Player, and Dealer classes.: 
How They Work and Which Are Worth It. (2025, November 5). WinStar World Casino and Resort. https://www.winstar.com/blog/blackjack-side-bets-guide-how-they-work-and-which-are-worth-it/

## Attribution Table

| Method/Function        | Primary Author   | Technique Claimed |
|------------------------|------------------|-------------------|
| Player.decide          | Nadisha Adikari  | 1. Conditional expressions |
| Player.place_bet       | Nadisha Adikari  | 11. Composition of two custom classes |
| Card.__add__           | Michael Ama      | 14. Magic methods other than __init__() |
| Pairs.__init__         | Michael Ama      | 10. super() |
| Dealer.hand_description| Sophia Pandey    | 3. F-strings containing expressions |
| Dealer.play_turn       | Sophia Pandey    | N/A |
| Dealer.show_hand       | Riley Tokofsky   | N/A |
| Deck.__init__          | Riley Tokofsky   | 2. Optional parameters and/or keyword arguments |
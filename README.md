Blackjack is a card game where the player tries to reach 21—or as close as possible—without going over, while competing against a dealer. Because the next card is unknown, the player must rely on judgment and chance to decide their moves. The game is commonly associated with gambling and winning money.

Players can take several actions: “hit” (take another card), “stand” (end their turn), “double down” (double their bet after the first two cards), “split” (turn a pair into two separate hands), and optional bets like insurance or Perfect Pairs. Each round starts with both the player and dealer receiving initial cards. The player then chooses actions until they stand or bust, while the dealer follows similar play. Rounds repeat until the player decides to stop.


Purpose of each file:
Card_Class: Defines a single playing card used in the game. Each card has a suit (Hearts, Diamonds, Clubs, Spades) and a rank/value. This class provides the basic building block for the deck system and is used throughout the program whenever cards are created, displayed, or evaluated for hand values.

Dealer_Class: Represents the dealer in the Blackjack game. The dealer interacts with the Deck_Class to draw cards and manages the dealer’s hand according to Blackjack rules. This class is responsible for automating dealer behavior during each round.

Deck_Class: Represents one or more shuffled decks of standard playing cards. This class is responsible for creating a full set of Card objects, shuffling them, and managing which cards have already been dealt. It provides functionality for drawing cards during gameplay and removes cards from the deck once used.

Player_Class: Represents the player in the game. This class manages the player’s hand, betting actions, and decisions such as hit or stand. It also calculates the player’s score and determines whether the player has won, lost, or busted during a round.


Annotated bibliography:
This source was used to understand the official rules of Blackjack, including player actions such as hit, stand, and double down. It helped guide the logic implemented in the Player and Dealer classes: 
Bicycle. (2025). Blackjack. Bicyclecards.com. https://bicyclecards.com/how-to-play/blackjack

This source helped with understanding how to structure classes in Python, which was needed for implementing the Card, Deck, Player, and Dealer classes.: 
How They Work and Which Are Worth It. (2025, November 5). WinStar World Casino and Resort. https://www.winstar.com/blog/blackjack-side-bets-guide-how-they-work-and-which-are-worth-it/
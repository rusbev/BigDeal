__author__ = 'Jake Mackay'
# A program for simulating the dealing of 13 cards to 4 people from a deck.


import random

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]

PLAYERS = ["North", "East", "South", "West"]

CARDS = 52
CARDS_PER_HAND = 13


def main():
    # Create a deck as a list of integers from 0 to 51
    deck = list(range(CARDS))

    # Shuffle the deck
    random.shuffle(deck)
    dealt = 0

    # Loops to deal until deck is empty
    for i in range(1, 14):
        print "Dealing hand #", dealt + 1
        dealt = dealt + 1
        # print(deck)

        # Loops to deal to table
        for j in range(0, 4):
            card = deck.pop(0)

            print PLAYERS[j], "got the", RANKS[card % CARDS_PER_HAND], "of", SUITS[card // CARDS_PER_HAND]
        print"\n"

    print"Whiskey was spilt, game was interrupted by necessary shootout"


main()

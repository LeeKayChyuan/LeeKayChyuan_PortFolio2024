from __future__ import annotations # for type hints of a class in itself
from enum import Enum


class Rank(Enum):
    """
    This class represents the ranks of a suit with 2 being the lowest and Ace being the highest.

    only one function that takes the Rank as an arguments and outputs 
    a boolean variable which tells us if the current rank is lower than another rank.
    """
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __lt__(self, other: Rank) -> bool:
        return self.value < other.value			


class Suit(Enum):
    """
    This class represents all the suits within the deck of cards.
    """
    Clubs = 1
    Diamonds = 2
    Spades = 3
    Hearts = 4

    def __lt__(self, other: Suit) -> bool:
        return self.value < other.value


class Card:
    """
    This Class Returns the card name as well as the card art.

    The __init__ function takes the Arguments:
     - Rank of the Card
     - Suit of the Card

    Returns the string value of the card name.
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        card_art = ''
        art = {
                    1: ["\n┌─────────┐", "│ 1       │", "│    ♣    │", '│       1 │', "└─────────┘"],
                    2: ["\n┌─────────┐", "│ 2       │", "│    ♦    │", '│       2 │', "└─────────┘"],
                    3: ["\n┌─────────┐", "│ 3       │", "│    ♠    │", '│       3 │', "└─────────┘"],
                    4: ["\n┌─────────┐", "│ 4       │", "│    ♥    │", '│       4 │', "└─────────┘"],
                    5: ["\n┌─────────┐", "│ 5       │", "│         │", '│       5 │', "└─────────┘"],
                    6: ["\n┌─────────┐", "│ 6       │", "│         │", '│       6 │', "└─────────┘"],
                    7: ["\n┌─────────┐", "│ 7       │", "│         │", '│       7 │', "└─────────┘"],
                    8: ["\n┌─────────┐", "│ 8       │", "│         │", '│       8 │', "└─────────┘"],
                    9: ["\n┌─────────┐", "│ 9       │", "│         │", '│       9 │', "└─────────┘"],
                    10: ["\n┌─────────┐", "│ 10      │", "│         │", '│      10 │', "└─────────┘"],
                    11: ["\n┌─────────┐", "│ J       │", "│         │", '│       J │', "└─────────┘"],
                    12: ["\n┌─────────┐", "│ Q       │", "│         │", '│       Q │', "└─────────┘"],
                    13: ["\n┌─────────┐", "│ K       │", "│         │", '│       K │', "└─────────┘"],
                    14: ["\n┌─────────┐", "│ A       │", "│         │", '│       A │', "└─────────┘"]}

        for a in range(5):
                if a == 0 or 4:
                        new = art[self.rank.value][a]
                if a == 1 or a == 3:
                        new = art[self.rank.value][a]
                elif a == 2:
                        new = art[self.suit.value][a]
                card_art += new
                card_art += "\n"
                
        return card_art
        
def __eq__(self, other: Card) -> bool:

        return self.suit == other.suit and self.rank == other.rank

def __lt__(self, other: Card) -> bool:
            if self.suit == other.suit:
                return self.rank < other.rank
            else:
                return self.suit < other.suit


# if __name__ == "__main__":
# 	card1 = Card(Rank.Two, Suit.Spades)
# 	card2 = Card(Rank.Ace, Suit.Hearts)

# 	print(f"{card1}, {card2}")

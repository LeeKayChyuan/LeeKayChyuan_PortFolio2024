from __future__ import annotations
from cards import Card, Rank, Suit


class Player:
	"""
	Player is the base player class that is being inherited by all Players. 

	It initialises the name, hand, round and total score.

	Returns None
	"""
	def __init__(self, name: str) -> None:
		self.name = name
		self.hand = []
		self.round_score = 0
		self.total_score = 0

	def __str__(self) -> None: 
		return self.name

	def __repr__(self) -> None: #
		return self.__str__()

	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> (bool, str):
		 """
		 this function checks the valid play of the card that is given.
		 
		 Arguments:
		 - card of the current card in hand
		 - trick which is the list of cards that has been played within the trick
		 - broken_hearts which is a boolean variable that is either True or False

		 Returns a tuple of the boolean variable and a string statement.
		 """
		 if trick == []:
			 for cards in range(len(self.hand)):
				 if cards == Card(Rank.Two, Suit.Clubs) and card != Card(Rank.Two, Suit.Clubs):
					 return (False, "Play is not Valid")
			 if broken_hearts == False and card.suit.name == "Hearts":
				 return (False, "Player cannot play Hearts before hearts have been broken!")
			 else:
				 return (True, "Play is valid")
		 else:
			 lead = trick[0]
			 for cards in self.hand:
				 if cards.suit == lead.suit and card.suit != lead.suit:
					 return (False, "Play is not Valid")
			 if cards.suit != lead.suit and card.suit.name == "Hearts":
				 return (True, "Play is valid")
			 else:
				 return (True, "Play is valid")


# if __name__ == "__main__":

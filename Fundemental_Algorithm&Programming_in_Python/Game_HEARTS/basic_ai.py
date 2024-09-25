from __future__ import annotations 
from cards import Card, Rank, Suit

class BasicAIPlayer:
	
	"""
	BasicAIPlayer class act as a player and participate in the game later.
	BasicAIPlayer will only play the smallest card on their hand and pass the 3 highest card
	"""
	def __init__(self, name: str) -> None:
		self.name= name
		self.hand = []
		self.round_score = 0
		self.total_score = 0
	
	def __str__(self) -> str:
		return self.name

	def __repr__(self) -> str:
		return self.__str__()	

	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> (bool, str):

		""" 
		Function used to check if the played card is a valid play. 

		Playing card of Hearts as lead is not allowed if the hearts hasn't broken yet.
		If there are same suit card as the lead card in player's hand but played a different suit card instead is not allowed.

		Arguments:
		- card: A Card object
		- trick: A list of Card objects
		- broken_hearts: A boolean to check if hearts have been broken

		Returns a boolean to check if the play is valid or not
		"""
		if trick == []:		# if playing as lead card
			for cards in range(len(self.hand)):
				if cards == Card(Rank.Two, Suit.Clubs) and card != Card(Rank.Two, Suit.Clubs):
					return False
				if broken_hearts == False and card.suit == "Hearts":
					return False
				else:
					return True
			else:
				lead = trick[0]
				for cards in self.hand:
					if cards.suit == lead.suit and card.suit != lead.suit:		# if not playing same suit as lead card
						return False
				if broken_hearts == False and card.suit == "Hearts":
					return False
				else:
					return True

	def play_card(self, trick: list[Card], broken_hearts: bool)-> Card:

		"""
		If player is playing as the lead card, the smallest value card will be played.
		Else, player will play the same suit card as the lead card with the smallest value is there is any.
		If the player's hand doesn't have card having same suit as lead card, 
		the card with smallest suit and smallest rank of the suit will be played

		Arguments:
		- trick: A list of Card objects
		- broken_hearts: A boolean to check if hearts are broken

		Returns a Card object which is the smallest card in hand
		"""

		smallest_val = 5		
		if trick == []:
			smallest_val = 5
			for cards in self.hand:	
				if cards.suit.value < smallest_val:		# play the smallest card if leading
					smallest_val = cards.suit.value
					smallest_card = cards
				elif cards.suit.value == smallest_val and cards.rank.value < smallest_card.rank.value:
					smallest_card = cards
			self.hand.remove(smallest_card)
			trick.append(smallest_card)
			return smallest_card
		else:
			lead = trick[0]				
			smallest_rank = 15
			same_suit = False
			same_suit_list = []
			for cards in self.hand:
				if cards.suit == lead.suit:
					same_suit == True
					same_suit_list.append(cards)
				elif same_suit == False and cards.suit != lead.suit:
					if cards.suit.value < smallest_val:
						smallest_val = cards.suit.value
						smallest_card = cards
					elif cards.suit.value == smallest_val and cards.rank.value < smallest_card.rank.value:
						smallest_card = cards
			if same_suit_list != []:
				smallest_card = same_suit_list[0]
				smallest_rank = smallest_card.rank.value
				for cards in same_suit_list:
					if cards.rank.value < smallest_rank:
						smallest_rank = cards.rank.value
						smallest_card = cards
			self.hand.remove(smallest_card)
			trick.append(smallest_card)
			return smallest_card
			

	def pass_cards(self) -> list[Card]:
		"""
		This function iterates through the cards in hand and takes the 3 highest value cards, appends them to highest_card_list 
		and removes them from the hand.

		Returns a list of Card objects
		"""
		highest_card_list = []
		for i in range(3):
			highest_suit = 0
			highest_rank = 0
			for cards in self.hand:
				if cards.suit.value > highest_suit:
					highest_suit = cards.suit.value
					highest_rank = cards.rank.value
					highest_card = cards
				elif cards.suit.value == highest_suit and cards.rank.value > highest_rank:
					highest_rank = cards.rank.value
					highest_card = cards
			highest_card_list.append(highest_card)
			self.hand.remove(highest_card)
		return highest_card_list


	# if __name__ == "__main__":
    # # Test your function here
    # # player = BasicAIPlayer("Test Player 1")
    # # player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
    # # trick, broken_hearts = [Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades)], False
    # # print(player.check_valid_play(player.hand[0], trick, broken_hearts))
    # 	pass

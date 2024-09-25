from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player

class BetterAIPlayer(Player):
	""" 
	BetterAIPlayer class is an improved BasicAIPlayer class which act as a player 
	and participate in the game later. It contained advance strategy so that it perform 
	better to increaase the difficulty of the game. 											
	"""

	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
		"""	
		This function is to choose the card to play in everyround, including the starting round 

		The main changes in play_card functions is 
		while trick == [] , the Ace(cards.rank.value == 14) will not be played in lead because 
		someone might voided that suit and give you Ace Heart or Queen Spades

		Arguments:
			- trick: A list of Card objects
			- broken_hearts: A boolean to check if hearts have been broken

		Returns a Card object that is the smallest card in the hand					
		"""
		smallest_val = 5
		if trick == []:
			smallest_val = 5
			for cards in self.hand:
				if cards.suit.value < smallest_val:
					if cards.rank.value == 14 :
						continue
					else :
						smallest_val = cards.suit.value
						smallest_card = cards
				elif cards.suit.value == smallest_val and cards.rank.value < smallest_val:
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
					elif cards.suit.value == smallest_val and cards.rank.value < smallest_val:
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
		This function is to pick 3 cards in hand to pass to the other players 

		The main changes in pass_cards function is player will not pass the 3 highest suit value but 
		pass the 3 highest rank value.
		Next, the 2Club will be choosen to pass because 2club determines which player starts, pass it 
		should let us to lead the next trick.
		Third the Ace of Hearts will not be passing down, because it has a guarantee point.			

		Arguments:
			- passing_to: A string to show who we are passing To

		Returns a list of Card objects to be passed to another player
		"""
		pass_card_list = []
		for i in range(3):
			pass_suit = 0
			pass_rank = 0
			for cards in self.hand:
				if cards.rank.value == 2 and cards.suit.value == 1:
					pass_card = cards
				elif cards.rank.value == 12 and cards.suit.value == 4:
					break
				elif cards.rank.value > pass_rank:
					pass_rank = cards.rank.value
					pass_card = cards
				elif cards.suit.value != pass_suit and cards.rank.value == pass_rank:
					pass_rank = cards.rank.value
					pass_card = cards
			pass_card_list.append(pass_card)
			self.hand.remove(pass_card)
		return pass_card_list

if __name__ == "__main__":
	
	player = BetterAIPlayer(Player)
	player.hand = [Card(Rank.Ace, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Hearts)]
	trick = []
	broken_hearts = False
	print(player.play_card(trick, broken_hearts))

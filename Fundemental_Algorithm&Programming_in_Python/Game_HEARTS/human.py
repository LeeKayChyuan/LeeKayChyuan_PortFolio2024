from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player

class Human(Player):
	
	def __init__(self, name):
		"""
		from the Parent class Player, we inherit the information of name, hand, round_score and total_score.
		where name takes the input of the player's name.	
		"""
		self.name = input('Please enter your name: ')
		self.hand = []
		self.round_score = 0
		self.total_score = 0
            # self.play_card(trick: list[Card], broken_hearts: bool)
            # self.pass_cards(passing_to)
		
	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
			"""
			This function prints out a hand and checks if the input for playing a card is a proper value
			it removes the card from the hand and returns it.

			Arguments: 
				- trick: A list of cards
				- broken_hearts: A boolean to check if hearts are broken

			Returns a card object
			"""
			print(self.print_hand())
			valid_input = False
			while valid_input == False:
				try:
					play_card = int(input('Select a card to play: '))

				except ValueError:
					print('Please enter an integer.')
					continue
				if play_card > len(self.hand) -1:
						print('Please select within the range.')
				else:
						card = self.hand[play_card]
						if self.check_valid_play(card, trick, broken_hearts)[0] == True:
							valid_input = True
						else:
							print(self.check_valid_play(card, trick, broken_hearts)[1])
			self.hand.remove(card)
			trick.append(card)
			return card

	def pass_cards(self, passing_to: str) -> list[Card]:
		"""
		This function first prints a the hand of the player is is prompt
		to choose 3 cards the player would like to pass, the user will input the cards
		and the function checks if it is a valid integer, within range of cards, is using proper commas and spacing 
		and is not repeating numbers. 

		Arguments:
			- str value of player that the cards are being passed to.

		Returns the List of Cards
		"""
		check_list = []
		print(f"Your current hand: ")
		print(self.print_hand())
		valid_input = False
		while valid_input == False:
			player_pass_list = []
			enter_int = True
			invalid_card = False
			check_dup = False
			pass_card = input(f"Select three cards to pass off to {passing_to} (e.g. '0, 4, 5'): ")
			pass_card = list(pass_card.split(','))
			if len(pass_card) != 3:
				print('Please choose 3 cards.')
				continue
			
			for i in pass_card:
				try:
					check_int = int(i)
					if check_int < len(self.hand):
						player_pass_list.append(self.hand[check_int])
					else:
						invalid_card = True
				except ValueError:
						enter_int = False
						continue
			for j in player_pass_list:
				if player_pass_list.count((j)) > 1:
					check_dup = True
			if enter_int == False or invalid_card == True or check_dup == True:
				if enter_int == False:
					print('Enter integers!')
				if invalid_card == True:
					print('Choose cards from your hand!')
				if check_dup == True:
					print('Choose 3 different cards!')
			elif enter_int == True and invalid_card == False and check_dup == False:
				for i in player_pass_list:
					self.hand.remove(i)
				valid_input = True
		return player_pass_list
	def print_hand(self):
		card_art = ''
		art = {
					1: ["┌─────────┐", "│ 1       │", "│    ♣    │", '│       1 │', "└─────────┘","     0      "],
					2: ["┌─────────┐", "│ 2       │", "│    ♦    │", '│       2 │', "└─────────┘","    1     "],
					3: ["┌─────────┐", "│ 3       │", "│    ♠    │", '│       3 │', "└─────────┘","     2      "],
					4: ["┌─────────┐", "│ 4       │", "│    ♥    │", '│       4 │', "└─────────┘","    3     "],
					5: ["┌─────────┐", "│ 5       │", "│         │", '│       5 │', "└─────────┘","     4     "],
					6: ["┌─────────┐", "│ 6       │", "│         │", '│       6 │', "└─────────┘","     5     "],
					7: ["┌─────────┐", "│ 7       │", "│         │", '│       7 │', "└─────────┘","     6      "],
					8: ["┌─────────┐", "│ 8       │", "│         │", '│       8 │', "└─────────┘","    7     "],
					9: ["┌─────────┐", "│ 9       │", "│         │", '│       9 │', "└─────────┘","     8     "],
					10: ["┌─────────┐", "│ 10      │", "│         │", '│      10 │', "└─────────┘","    9     "],
					11: ["┌─────────┐", "│ J       │", "│         │", '│       J │', "└─────────┘","     10    "],
					12: ["┌─────────┐", "│ Q       │", "│         │", '│       Q │', "└─────────┘","     11    "],
					13: ["┌─────────┐", "│ K       │", "│         │", '│       K │', "└─────────┘","     12    "],
					14: ["┌─────────┐", "│ A       │", "│         │", '│       A │', "└─────────┘","     13   "]}

		for a in range(6):
			for i in range(len(self.hand)):
				if a == 0 or 4:
						new = art[self.hand[i].rank.value][a]
				if a == 1 or a == 3:
						new = art[self.hand[i].rank.value][a]
				elif a == 2:
						new = art[self.hand[i].suit.value][a]
				else: 
						new = art[i+1][a]
				card_art += new
			card_art += "\n"
				
		return card_art
				

# if __name__ == "__main__":
# 	Player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
# 	player = Human(Player)
# 	player.pass_cards("Player 2")
# 	print(Player.hand)
	
	

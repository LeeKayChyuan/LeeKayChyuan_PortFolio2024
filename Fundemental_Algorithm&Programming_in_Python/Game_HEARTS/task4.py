from __future__ import annotations
import random
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from round import Round
import copy

class Hearts:
	""" class Hearts is the function that runs the game with basic ai players """
	def __init__(self) -> None:
		""" 
		This function initializes the Heart class and asks the user to input the target score and number of players
		it then creates a list of BasicAIPlayers according to the number of players
		while the round is not over, it increments the round and creates a new deck and deals cards to players
		it then runs the game by making each player pass and play and ends when target score has been reached
		"""
		def int_input(prompt="", restrict=None):
			""" 
			This function modifies the input command which allows us to throw an exception whenever user inputs an improper value
			it also allows for restriction of the values that it accepts
			
			Arguments:
			  - prompt: A parameter which accepts string as an argument
			  - restrict:  Allows user to pass a list of integers as an argument which restricts the users choice when inputting
			
			Returns an integer
			"""
			while True:
				choice = input(prompt)
				try:
					int_choice = int(choice)
				except ValueError:
					print("Please enter a valid number!")
					continue
				if restrict is None:
					break
				elif int_choice in restrict:
					break
				elif int_choice < 3 or int_choice > 5:
					print("Please entere a valid number between 3 to 5!")
					continue
			return int_choice	

		self.target = int_input("Please enter a target score to end the game:")
		self.playerno = int_input("Please enter the number of players (3-5):", [3,4,5])

		self.players = []
		x = 1
		while len(self.players) != self.playerno:
			self.players.append(BasicAIPlayer(f"Player {x}"))
			x+=1

		self.round = 0
		round_over = False
		while round_over == False:
			self.round += 1 
			self.deck = [Card(rank,suit) for rank in Rank for suit in Suit]
			print(f"========= Starting round {self.round} =========")
			self.deal(self.deck, self.playerno, self.players)
			pdict = {'player_name': 'player', 'who_to_pass': 'pass_order[i]', 'pass_list':'cards'}
			passing = []
			self.le_pass()
			for player in self.players:
				who_to_pass = self.check_pass(player)
				self.pass_order.append(who_to_pass)
				index = self.players.index(player)
				passing.append(pdict.copy())
				passing[index]['player_name'] = player
				passing[index]['who_to_pass'] = self.pass_order[index]
				passing[index]['pass_list'] = self.pass_list[index]	
			
			for player in passing:
				print(f"{player['player_name']} passed {player['pass_list']} to {player['who_to_pass']}")
			self.le_pass()
			Round(self.players)
			print(f"========= End of round {self.round} =========")
			shot_moon = False
			winning_player = ""
			winning_score = self.target * 2
			same_score = False
			for player in self.players:
				if player.round_score == 26:
					print(f"{player} has shot the moon! Everyone else receives 26 points")
					shot_moon = True
			if shot_moon == True:
				for player in self.players:
					if player.round_score == 26:
						player.round_score = 0
					else:
						player.round_score = 26
			for player in self.players:
				player.total_score += player.round_score
				player.round_score = 0
				print(f"{player}'s total score: {player.total_score}")
			for player in self.players:
				if player.total_score >= self.target:
					for player in self.players:
						if player.total_score == winning_score:
							same_score = True
						elif player.total_score < winning_score:
							winning_score = player.total_score
							same_score = False
							round_over = True
							winning_player = player

			if same_score == False and round_over == True:	
				print(f"{winning_player} is the winner!")

	def deal(self, deck, playerno, players):
		""" 
		This function shuffles and deals cards to the player and checks if the deal is legal/valid
		if not(meaning a player does not have a card in hand that is not hearts or queen of spades) it remakes a new deck and reshuffles it
		it also removes cards according to how many players are playing(3 remove Two of Diamonds, 5 remove Two of Diamonds & Two of Spades. 
		
		Arguments:
		  - deck: A deck of cards which is a list of all 52 cards
		  - playerno: The amount of players 
		  - players: A list of player objects

		Appends cards to players hand and prints out what they are dealt 
		"""	
		valid_deal = False
		while valid_deal != True:
			new_deck = copy.deepcopy(deck)
			random.shuffle(new_deck)

			if self.playerno == 3:
				new_deck.remove(Card(Rank.Two,Suit.Diamonds))
			elif self.playerno == 5:
				new_deck.remove(Card(Rank.Two,Suit.Diamonds))
				new_deck.remove(Card(Rank.Two,Suit.Spades))
		
			while len(new_deck) != 0:       
				for player in players:
					player.hand.append(new_deck[0])
					new_deck.remove(new_deck[0])		
				
			for player in players:
				count = 0
				for card in player.hand:
					if (card.suit.name == 'Spades' and card.rank.name == 'Queen') or card.suit.name == 'Hearts':
						count += 1
				if count == len(player.hand):
					valid_deal = False
					continue
				else:
					valid_deal = True
			
			for player in players:
				print(f"{player} was dealt {player.hand}")
    
	def check_pass(self, player):
		"""
		This function checks for who the player should pass to in the current round.

		Arguments:
		  - player: The current player object who is passing

		Returns a player object of who we are passing to
		"""
		temp_round = copy.deepcopy(self.round)
		if temp_round > len(self.players):
			temp_round = temp_round % len(self.players)
		
		index = temp_round + self.players.index(player)

		if index > (len(self.players)-1):
			pass_to = temp_round + self.players.index(player) - len(self.players)
		else:
			pass_to = temp_round + self.players.index(player)

		return self.players[pass_to] 
			
	def le_pass(self):
		"""
		This function creates a pass_list list and pass_order list to indicate how passing should work this round
		it checks and appends how players should be ordered in pass_order and passes from each specific player to the on they should pass to
		then it passes the cards in pass_list to the respective players

		Appends card from pass_list to player objects in order of pass_order
		"""
		self.pass_list = []
		for player in self.players:
			self.pass_list.append(BasicAIPlayer.pass_cards(player))

		self.pass_order = []
		for player in self.players:
			self.pass_order.append(self.check_pass(player))
			
		for player in self.pass_order:
			for card_list in self.pass_list:
				if self.pass_order.index(player) == self.pass_list.index(card_list):
					for card in card_list:
						player.hand.append(card)



if __name__ == "__main__":
	Hearts()

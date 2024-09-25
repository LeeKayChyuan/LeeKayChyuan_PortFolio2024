from __future__ import annotations
import random
import copy
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from better_ai import BetterAIPlayer
from player import Player
from round import Round
from human import Human

class Hearts:
        print('Welcome to ♥ HEARTS ♥')
        

        def __init__(self) -> None:
            """
            This function initializes a list of players with 1 human, 2 basic_ai and 1 better_ai
            and sets a target score then calls for print_round which prints out the round
            """
            self.players = [Human(Player), BasicAIPlayer('Robot 1'), BasicAIPlayer('Robot 2'), BetterAIPlayer('Bob')]
            self.target = 100
            self.print_round()

        def print_round(self):
                """
                this function initiates the game. 
                The round is initalised as 0 and round_over is set to False
                The round counter increases each start of a round, 
                deck is initialised with 52 cards objects.
                The cards are shuffled and dealt to the players using the deal() function.
                a dictionary is made to keep track of player objects, which player objects they are passing to and 
                the list of cards that they will pass.
                Once the cards are passed, the round gets called to begin the round sequence. 
                Once round ends, check if "player has shot the moon!" and sets the score acordingly
                Finally, the round score of each player gets tallied to their total score. 
                """
                self.round = 0
                round_over = False
                playerno = len(self.players)
                while round_over == False:
                        self.round += 1 
                        self.deck = [Card(rank,suit) for rank in Rank for suit in Suit]
                        print(f"========= Starting round {self.round} =========")
                        self.deal(self.deck, playerno, self.players)
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
                                if player['player_name'] == self.players[0]:
                                        passing_to = player['who_to_pass']
                                # print(f"{player['player_name']} passed {player['pass_list']} to {player['who_to_pass']}")
                        
                        self.le_pass()
                        for player in self.players:
                                try:    
                                        player.pass_cards(passing_to)
                                except TypeError:
                                        continue
                        Round(self.players)
                        print(f"========= End of round {self.round} =========")
                        shot_moon = False
                        winning_player = ""
                        winning_score = self.target * 2
                        same_score = False
                        # for player in self.players:
                        # 	print(player.round_score)
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

                        if playerno == 3:
                                new_deck.remove(Card(Rank.Two,Suit.Diamonds))
                        elif playerno == 5:
                                new_deck.remove(Card(Rank.Two,Suit.Diamonds))
                                new_deck.remove(Card(Rank.Two,Suit.Spades))
                
                        while len(new_deck) != 0:       
                                for player in players:
                                        player.hand.append(new_deck[0])
                                        new_deck.remove(new_deck[0])		
                        # check if each player has at least one card that is not Queen of Spades or Hearts
                                
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

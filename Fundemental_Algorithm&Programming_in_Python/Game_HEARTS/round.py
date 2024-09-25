from __future__ import annotations
from cards import Card, Rank, Suit
import copy
import time

class Round:
    """
    class Round is to execute the gameplay of the game Hearts and prints 
    the output of the player's play.
    we iterate throught the length of players list based on the order of play and
    if player takes the trick, it will add the penalty point into the player's round score.

    Beginning of the first round, we identify the player with the 'Two of Clubs' to begin the game 
    and will lead the game followed by the next player and loop.

    We use two lists, skipped_player and player_list, two iterate the game where player_list contains the player 
    with the starting trick and the next player in the player list followed by the players we had skipped if they did not have the starting card. 
    """
    def __init__(self, players: list[Player]) -> None:
            self.players = players
            self.execution(players)

    def execution(self, players):
            rounds = 0
            self.broken_hearts = False
            while rounds <= len(players[0].hand):
                    round_end = False
                    self.trick = []
                    skipped_player = []
                    order_list = []
                    player_list = players.copy().copy()
                    break_flag = False
                    if rounds == 0:
                            for player in players:
                                    for card in player.hand:
                                            if card.suit.name == 'Clubs' and card.rank.name == 'Two':
                                                    played_card = Card(Rank.Two, Suit.Clubs)
                                                    player.hand.remove(card)
                                                    self.trick.append(played_card)
                                                    order_list.append(player)
                                                    player_list.remove(player)
                                                    print(f"{player} leads with {played_card}")
                                                    break_flag = True
                                                    break
                                    if break_flag == True:
                                            break
                                    else: 
                                            skipped_player.append(player)
                                            player_list.remove(player)
                            time.sleep(1)
                            for player in player_list:
                                    played_card = player.play_card(self.trick, self.broken_hearts)
                                    self.play_smallest(player,self.trick,self.broken_hearts,played_card,order_list)
                                    time.sleep(1)
                            for player in skipped_player:
                                    played_card = player.play_card(self.trick, self.broken_hearts)
                                    self.play_smallest(player,self.trick,self.broken_hearts,played_card,order_list)
                                    time.sleep(1)
                            taker = self.check_taker(self.trick,order_list)
                            penalty = self.check_penalty(self.trick)
                            print(f"{taker} takes the trick. Points received: {penalty}")
                            taker.round_score += penalty
                            
                            rounds += 1
                            round_end = True
                    else:
                            for player in players:
                                    if taker == player:
                                            played_card = player.play_card(self.trick, self.broken_hearts)
                                            self.play_smallest(player,self.trick,self.broken_hearts,played_card,order_list)
                                            player_list.remove(player)  
                                        #     order_list.append(player)
                                        #     player_list.remove(player)
                                        #     print(f"{player} leads with {played_card}")
                                    else:
                                            skipped_player.append(player)
                                            player_list.remove(player)
                            time.sleep(1)

                            for player in player_list:
                                    played_card = player.play_card(self.trick, self.broken_hearts)
                                    self.play_smallest(player,self.trick,self.broken_hearts,played_card,order_list)
                                    time.sleep(1)
                            for player in skipped_player:
                                    played_card = player.play_card(self.trick, self.broken_hearts)
                                    self.play_smallest(player,self.trick,self.broken_hearts,played_card,order_list)
                                    time.sleep(1)
                            taker = self.check_taker(self.trick,order_list)
                            penalty = self.check_penalty(self.trick)
                            print(f"{taker} takes the trick. Points received: {penalty}")
                            taker.round_score += penalty
                            

    def play_smallest(self,player,trick,broken_hearts,played_card,order_list):
            """
            this function outputs the played card by the player of that round, 
            adding the card played to the trick list and adding the player to another list called the order_list which
            will be use to determine who takes the next trick and the order of the round after.

            we check for another condition where the player doesnt have the a card of the same suit as the trick and if played
            a card in the suit of Hearts, will print out the statement "Hearts have been broken!"
            """
            if order_list == []:
                    print(f"{player} leads with {played_card}")
            else:
                    print (f"{player} plays {played_card}")
            if self.trick != [] and played_card.suit.name == 'Hearts' and self.broken_hearts == False:
                    self.broken_hearts = True
                    print("Hearts have been broken!")
            order_list.append(player)



    def check_penalty(self,trick):
            """
            checks if the card played contain a suit of Hearts or is a Queen of Spades
            and calculates the total penalty points the trick taker will recieve. 
            """
            penalty = 0
            for current_card in self.trick:
                    if current_card.suit.name == 'Hearts':
                            penalty += 1
                    elif current_card.suit.name == 'Spades' and current_card.rank.name == 'Queen':
                            penalty += 13
            return penalty

    def score(self,players):
            for player in players:
                    print(f"{player}'s score: {player.round_score}")
                    player.total_score += player.round_score
                    player.round_score = 0

    def check_taker(self,trick,order_list):
            lead = self.trick[0]
            taker = order_list[0]
            highest_card = lead	
            for i in range(len(self.trick)):
                    current_card = self.trick[i]
                    if current_card.suit == lead.suit and current_card.rank > highest_card.rank:
                            highest_card = current_card
                            taker = order_list[i]
            return taker

if __name__ == '__main__':
	players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"), BasicAIPlayer("Player 4")]
	players[0].hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ace, Suit.Hearts)]
	players[1].hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades), Card(Rank.Six, Suit.Diamonds)]
	players[2].hand = [Card(Rank.Seven, Suit.Diamonds), Card(Rank.Ace, Suit.Spades), Card(Rank.Jack, Suit.Diamonds), Card(Rank.Queen, Suit.Spades)]
	players[3].hand = [Card(Rank.Queen, Suit.Hearts), Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Diamonds), Card(Rank.King, Suit.Hearts)]
	
	Round(players)

"""
Group name: Team fruit loops
Authors:  Brian Ooi Say Yew, Ku Mohamad Ilhan, Hui Ying Wong, Kay Lee
"""

import time
import random

def display_rules():
  print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)
  input("Press enter to go back")
  return


def display_main_menu():
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")


def int_input(prompt="", restricted_to=None):
  """
  Helper function that modifies the regular input method,
  and keeps asking for input until a valid one is entered. Input 
  can also be restricted to a set of integers.

  Arguments:
    - prompt: String representing the message to display for input
    - restricted: List of integers for when the input must be restricted
                  to a certain set of numbers

  Returns the input in integer type.
  """
  while True:
    player_input = input(prompt)
    try:
      int_player_input = int(player_input)
    except ValueError:
      continue
    if restricted_to is None:
      break
    elif int_player_input in restricted_to:
      break

  return int_player_input


def cpu_player_choice(score):
  """
  This function simply returns a choice for the CPU player based
  on their score.

  Arguments:
    - score: Int

  Returns an int representing a choice from 1, 2 or 3.
  """
  time.sleep(2)
  if score < 14:
    return 1
  elif score < 17:
    return 3
  else:
    return 2

#Task 1
def display_game_options(player:list):
    player_no = player['name']
    score = player['score']
    print(f"------------{player_no}'s turn------------")
    print(f"{player_no}'s score: {score}")
    print('1. Roll')
    print('2. Stay')
    if at_14(score)==True:
        print('3. Roll One')    

def display_round_stats(round: int, players: list):
    print(f"-----------Round {round}-----------")
    for each_player in players:
        player_no = each_player['name']
        score = each_player['score']
        print(f"{player_no} is at {score}")

def at_14(score):
    if score >= 14:
        return True
    return False

#Task 2
def roll_dice(num_of_dice=1): 
  num = [] #set num as an empty set
  for i in range(num_of_dice): #loop number of dice insert by player
      num += [random.randint(1,6)] #a random numeber between 1 to 6 is choosen and stored in num 
  art = ''  #set art as an empty set 

  for a in range(5): #loop the rows of die to rearrange the order of die_art
      for i in range(len(num)):  #loop the rows of dice according to the number of die 
        new = die_art[num[i]][a]  #new row is stored in new 
        art += new #each row is stored in art 
      art += '\n' #\n is added after every row is stored in art

  return num, art 

die_art = {
  1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
  2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
  3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
  4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
  5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
  6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
} 

#TASK 3
def rolling_one(player): 
  print("Rolling one...") #prints the statement of the dice roll
  player['stayed'] = False #updates the stayed key to false since the user has chosen to roll
  result = roll_dice() # uses the roll_dice() function from task 2 to obtain the random roll and art
  print(result[1]) #prints the die art for the random roll
  player['score'] += result[0][0] #adds the value of the dice roll to the score key 
  return results(player) 

def rolling_both(player): 
  print("Rolling both...") #prints out the statement of the dice roll
  player['stayed'] = False #updates the stayed key to false since the user has chosen to roll
  result = roll_dice(2)#uses the roll dice() function from task 2 to obtain a random roll, we use 2 to indicate the amount of dice used.
  print(result[1]) #print the die art 
  player['score'] += result[0][0] + result[0][1] #takes the value of the 2 random dice rolls and adds both to the player score
  return results(player) 

def results(player): #checks the score of the player
  if player['score'] < 14: #checks if the score is less than 14 
    player['at_14'] = False #updates the at_14 key to false
    print(player['name'],"is now on ", player['score']) #prints out the statement of the players updated score
    return player
  else:   #when the player score is above or equals to 14
    player['at_14'] = True #updates the at_14 key to true
    print(player['name'],"is now on ", player['score']) #prints out the statement of the players updated score
    return check_bust(player) #brings to check if the score is above 22
     

def check_bust(player): #checking the bust if the player score is above 22 
  if player['score'] >= 22: #checks if the score is above or equals to 22
    player['bust'] = True #updates the bust key of the player to true
    print(player['name'], "goes bust!") # print the statement saying the player has gone bust
    return player
  else:
    return player
  
def stay(player): #player stays and doesnt roll
  print(player['name'],"has stayed with a score of ", player['score']) #prints statement saying player has stayed
  player['stayed'] = True  #sets player flag to true
  return player #returns the player dictionary 

def execute_turn(player, player_input): #main program to run the dice
  if player_input == 1:
    return rolling_both(player) #brings the player to rolling dice
  if player_input == 2:
    return stay(player) #brings the player to the stay position
  if player_input == 3:
    return rolling_one(player) #brings the player to the single roll 

# Task 4
def end_of_game(players):   # end_of_game function to check if game has ended and return true if it has or false if it has not
    max_score = -1   # declare and initialize max_score with value -1 (this is so that if a player decides to stay at the beginning and everyone else busts, that player will win since they are closest to 21)
    same_score = False  # declare and initialize boolean variable same_score with value False
    winner = "" # declare and initialize string variable winner to store name of winner
    busts = 0   # declare and initialize busts variable to check for number of busts

    for i in range(len(players)):   # iterates through list of players
        check_bust = players[i].get('bust') # declares variable check_bust and assigns value of key 'bust'
        check_stayed = players[i].get('stayed') # declares variable check_stayed and assigns value of key 'stayed'
        if check_bust != True:  # if player is not bust
            if check_stayed == True:    # and if player stayed
                if max_score == players[i].get('score'):  # and if max_score has another same score
                    same_score = True   # toggle boolean same_score to True
                elif max_score < players[i].get('score'):     # else if max_score less than score in dictionary
                    same_score = False  # toggle same_score to False
                    max_score = players[i].get('score') # assign current highest score in current iteration to variable max_score
                    winner = players[i].get('name') # assign value of key 'name' to winner variable
            elif check_stayed != True:  # else if player has not stayed
                return False    # return a False and end function (this allows players to continue playing)
        elif check_bust == True:    # else if player busts
            busts += 1  # add a one to the busts counter
    if busts == len(players):   # check if number of busts is equal to the amount of players 
        print("Everyone's gone bust! No one wins :(")  # if true, output "everyone is bust"
        return True # return True and end function 
    elif same_score == True:    # else if the boolean same_score has a value of True (this means that there are more than 1 highest scores)
        print("The game is a draw! No one wins :(") # outputs that the game is a draw
        return True #returns True and ends the function
    else:   # if none of the above is true, where there is no same score and not all players are bust
        print(winner + " is the winner!") # output max score and winner
        return True # return True and end the function

#Task 5
def solo_game():    # solo game function to play a game against an AI
    game_over = False   # declares and initialize variable game_over to check if game is over and sets it to False
    round = 0   # declare and initialize variable round to 0 (shown in sample output that round starts at 0)
    players = [{'name': 'Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}, {'name': 'Cpu', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}] # create a player list that stores two player dictionaries, one for the user and one for the cpu
    
    while game_over != True:    # while loop that loops until game_over is True
        display_round_stats(round, players) # outputs the round statistics
        if players[0]['stayed'] != True and players[0]['bust'] != True: # checks if user has not stayed and is not bust
            display_game_options(players[0])    # calls the display_game_options function which outputs options for the player to choose from
            player_input = int_input("Please enter an option: ", [1, 2, 3])    # declare and initialize player_input and prompt player to input a number which is restricted to 1, 2, 3 and stores it in player_input
            players[0] = execute_turn(players[0], player_input) # calls the execute_turn function and pass arguments of user's index and their input and updates the user index's player object
            display_game_options(players[1])    # calls the display_game_options function which outputs options for the player to choose from
            cpu_input = cpu_player_choice(players[1]['score'])  # calls the cpu_player_choice function which was given in the skeleton and stores it in cpu_input
            players[1] = execute_turn(players[1], cpu_input)    # calls the execute_turn function and passes arguments of cpu player's index and their input and updates the cpu player index's object
            game_over = end_of_game(players)    # calls the end_of_game(players) function to check if the game has ended and assigns its return value to game_over 
            round += 1  # if game is not over then increment round by 1
        elif (players[0]['stayed'] == True or players[0]['bust'] == True) and (players[1]['bust'] != True and players[1]['stayed'] != True):    # checks if user (has stayed or is bust) and if cpu (is not bust and has not stayed)
            display_game_options(players[1])    # calls the display_game_options and outputs options for cpu to choose from
            cpu_input = cpu_player_choice(players[1]['score'])  # calls the cpu_player_choice function and assigns the value to cpu_input
            players[1] = execute_turn(players[1], cpu_input)    # calls the execute_turn function and passes arguments of cpu player's index and their input
            game_over = end_of_game(players)    # calls the end_of_game(players) function to check if game is over and assigns its value to game_over 
            round += 1  # if game is not over then increment round by 1
        else:   # else statement for if user is bust or has stayed and cpu is bust or has stayed
            game_over = end_of_game(players)    # calls the end_of_game function to check if game has ended and assigns its return value to game_over

#Task 6
def create_list(num_of_players:int)-> list: # 
    players =[] # creates an empty list and assigns it to variable players
    player_dict = {'name':'Player','score':0,'stayed':False,'at_14':False,'bust':False} # creates a template for player dictionaries and assigns it to player_dict
    for i in range(num_of_players): # for loop which iterates through number of players which is given from num_of_players function
        players.append(player_dict.copy())  # appends the template from player_dict and creates copies of it and stores it into the players list
        players[i]['name']=f'Player {i+1}'  # assigns value of player's name to the key 'name' in the copies of dictionary objects within the players list and increments the number based on number of players 
    return players

def multiplayer_game(num_of_players):
    game_over = False
    create_list(num_of_players)  #create a list of player dictionary
    players = create_list(num_of_players) #the player list is created and returned back to the function
    round = 0   #initialize the round to 0
    while game_over != True: #while the game has not ended yet
        display_round_stats(round,players)   #display the round statement
        for i in range(len(players)):    #iterate over all of the players
          if (players[i]['bust']==False and players[i]['stayed'] == False) and end_of_game(players) == False:
            display_game_options(players[i])#display options for the players
            score = players[i]['score']
            player_input = int_input(("Please enter an option: "),(1, 2, 3))   #prompt input from the user as their choice
            execute_turn(players[i], player_input)  #execute player's choice
        game_over = end_of_game(players)    #check whether the game has ended
        round+=1    #next round
      
#Task 7
def main():
  exit_game = False # intialises the exit_game bool to be set at false
  while exit_game != True:  # a while loop to run the mainmenu display while exit_game is false
    display_main_menu() # displays the main menu provided by the skeleton code
    choice = int_input("Please enter an option: ") # prompts the user to chose the action based on the menu
    if choice == 1: # if player chooses to run the game solo
      solo_game()    # runs the game in singleplayer against the cpu
    elif choice == 2:   # if player chooses to play multiplayer
      num_of_players = int_input("Please enter the number of players: ")   # user is prompt to input the number of players and stores that value in num_of_players
      multiplayer_game(num_of_players)   # runs the multiplayer game with the number of players entered
    elif choice == 3:   # if user chooses to display the rules
      display_rules()    # outputs the rules 
    else:   # we assume the user puts in 4, which is to exit game
      print("Thanks for playing!")  # greeted with a thank you message
      exit_game = True  # changes the exit_game bool to true thus, terminating the game.

main()


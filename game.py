# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars, compare

# set up some variables for gameVars.player and AI lives
gameVars.player_lives = 5
gameVars.computer_lives = 5 

# gameVars.choices is an array => an array is a container that can hold multiple vaalues
gameVars.choices = ["rock", "paper", "scissors"]

# set the gameVars.computer variable to one of these gameVars.choices
gameVars.computer = gameVars.choices[randint(0, 2)]

# set up the game loop so that we dont have to restart all the time
gameVars.player = False

while gameVars.player is False:
	# set gameVars.player to true
	print("*****************\n")
	print("Computer lives: ", gameVars.computer_lives, "/5\n")
	print("Player lives: ", gameVars.player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("*****************\n")

	gameVars.player = input("choose rock, paper or scissors: ")
	gameVars.player = gameVars.player.lower()

	print("computer chose", gameVars.computer, "\n")
	print("player chose", gameVars.player, "\n")

	### this is where you would call compare
	
	### end compare stuff

	# handle all lives lost for gameVars.player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")
		#print("Out of lives! Good try. Would you like to play again?\n")
		#hoice = input("Y / N")
		#print(choice)

		#if (choice is "N") or (choice is "n"):
		#	print("You chose to quit")
		#	exit()

		#elif (choice is "Y") or (choice is "y"):
			# reset the game so that we can start all over again
		#	gameVars.player_lives = 5
		#	gameVars.computer_lives = 5
		#	gameVars.player = False
		#	gameVars.computer = gameVars.choices[randint(0, 2)]

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
		#print("gameVars.Computer is out of lives! Good game. Would you like to play again?\n")
		#choice = input("Y / N")
		#print(choice)

		#if (choice is "N") or (choice is "n"):
		#	print("You chose to quit")
		#	exit()

		#elif (choice is "Y") or (choice is "y"):
			# reset the game so that we can start all over again
		#	gameVars.player_lives = 5
		#	gameVars.computer_lives = 5
		#	gameVars.player = False
		#	gameVars.computer = gameVars.choices[randint(0, 2)]

	else:
		# need to check all of our conditions after checking for a tie
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]
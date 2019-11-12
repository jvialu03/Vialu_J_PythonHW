# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars

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
	print("gameVars.Computer lives: ", gameVars.computer_lives, "/5\n")
	print("gameVars.Player lives: ", gameVars.player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("*****************\n")

	gameVars.player = input("choose rock, paper or scissors: ")
	gameVars.player = gameVars.player.lower()

	print("gameVars.computer chose", gameVars.computer, "\n")
	print("gameVars.player chose", gameVars.player, "\n")

	if gameVars.player.lower() == "quit":
		exit()

	elif gameVars.computer == gameVars.player:
		print("tie! no one wins, play again")

	elif gameVars.player.lower() == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif gameVars.player.lower() == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif gameVars.player.lower() == "scissors":
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")

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
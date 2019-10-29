# import the random package so that we can generate a random choice
from random import randint

# set up some variables for player and AI lives
player_lives = 5
computer_lives = 5 

# choices is an array => an array is a container that can hold multiple vaalues
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

# set up the game loop so that we dont have to restart all the time
player = False

while player is False:
	# set player to true
	print("*****************\n")
	print("Computer lives: ", computer_lives, "/5\n")
	print("Player lives: ", player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("*****************\n")

	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("computer chose", computer, "\n")
	print("player chose", player, "\n")

	if player.lower() == "quit":
		exit()

	elif computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "covers", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else:
		print("That's not a valid choice, try again")

	# handle all lives lost for player or AI
	if player_lives is 0:
		print("Out of lives! Good try. Would you like to play again?\n")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("You chose to quit")
			exit()

		elif (choice is "Y") or (choice is "y"):
			# reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choices[randint(0, 2)]

	elif computer_lives is 0:
		print("Computer is out of lives! Good game. Would you like to play again?\n")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("You chose to quit")
			exit()

		elif (choice is "Y") or (choice is "y"):
			# reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choices[randint(0, 2)]

	else:
		# need to check all of our conditions after checking for a tie
		player = False
		computer = choices[randint(0, 2)]
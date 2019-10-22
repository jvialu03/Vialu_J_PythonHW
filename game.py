# import the random package so that we can generate a random choice
from random import randint

# choices is an array => an array is a container that can hold multiple vaalues
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

# set up the game loop so that we dont have to restart all the time
player = False

while player is False:
	# set player to true
	player = input("choose rock, paper or scissors\n")

	print("computer chose", computer, "\n")
	print("player chose", player, "\n")

	if player == "quit":
		exit()

	elif computer == player:
		print("tie! no one wins, play again")

	# need to check all of our conditions after checking for a tie
	player = False
	computer = choices[randint(0, 2)]
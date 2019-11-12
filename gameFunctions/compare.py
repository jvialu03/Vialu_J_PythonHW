from gameFunctions import gameVars

# what are you trying to comapre inside this function?
# you will need to pass those things in as arguments inside the round brackets
def comparechoices(playerchoice, AIchoice):
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
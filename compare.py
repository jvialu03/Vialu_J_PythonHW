from gameFunctions import gameVars

# what are you trying to comapre inside this function?
# you will need to pass those things in as arguments inside the round brackets
def comparechoices(playerChoice, AIchoice):
	if playerChoice == AIchoice:
		print("tie! no one wins, play again")

	elif playerChoice == "rock":
		if AIchoice == "paper":
			print("*You lose!", AIchoice, "covers", playerChoice,"*" "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("*You win!", playerChoice, "smashes", AIchoice,"*" "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif playerChoice == "paper":
		if AIchoice == "scissors":
			print("*You lose!", AIchoice, "cuts", playerChoice,"*" "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("*You win!", playerChoice, "covers", playerChoice,"*" "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif playerChoice == "scissors":
		if A == "rock":
			print("*You lose!", AIchoice, "smashes", playerChoice,"*" "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("*You win!", playerChoice, "cuts", AIchoice,"*" "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")
from random import randint
from gameFunctions import gameVars
# Define a python function that takes an argument
def winorlose(status):
	print("called win or lose")
	print("*****************\n")

	print("You", status, "! Would you like to play again?")

	gameVars.choice = input("Y / N")
	print(gameVars.choice)

	if (gameVars.choice is "N") or (gameVars.choice is "n"):
		print("You chose to quit")
		exit()

	elif (gameVars.choice is "Y") or (gameVars.choice is "y"):
		# reset the game so that we can start all over again
		global player_lives
		global computer_lives
		global player
		global computer
		global choices

		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.total_lives = 1
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]

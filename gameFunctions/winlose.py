from random import randint
# Define a python function that takes an argument
def winorlose(status):
	print("called win or lose")
	print("*****************\n")

	print("You", status, "! Would you like to play again?")

	choice = input("Y / N")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit")
		exit()

	elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
		global player_lives
		global computer_lives
		global player
		global computer
		global choices

		player_lives = 5
		computer_lives = 5
		player = False
		computer = choices[randint(0, 2)]

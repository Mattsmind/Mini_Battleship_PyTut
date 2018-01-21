#!/usr/bin/python3
#=============================================
# Mini Battleship
#=============================================
#
#  Simple straigh forward battleship game
#  built from a tutorial on codecademy, and
#  updated for Python 3.5.2.
#  Simple game, fun, and easy to code.

from random import randint

board = []

# CREATE OUR BOARD AND DISPLAY IT
for x in range(0,5):
	board.append(["O"] * 5)

def print_board(board):
	"""Print a cleaned up version of our board."""
	for row in board:
		print(" ".join(row))

# PICK OUR SHIPS LOCATION
def random_row(board):
	"""Pick a random row coordinate for our ship."""
	return randint(0, len(board) - 1)

def random_col(board):
	"""Pick an random column coordinate for our ship."""
	return randint(0, len(board) -1)

print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)
#DEBUG#
#print(ship_row)
#print(ship_col)

# BEGIN OUR LOOP
for turn in range(4):

	# GATHER USER INPUT
	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Column: "))

	# CHECK OUR GUESS
	if guess_row == ship_row and guess_col == ship_col:
		print("Congratulations! You sank my battleship!")
		print("""
 __        ___                       
 \ \      / (_)_ __  _ __   ___ _ __ 
  \ \ /\ / /| | '_ \| '_ \ / _ \ '__|
   \ V  V / | | | | | | | |  __/ |   
    \_/\_/  |_|_| |_|_| |_|\___|_|   
                                     
""")
		break
	else:
		if guess_row not in range(5) or guess_col not in range(5):
			print("Oops, that's not even in the ocean.")
		elif board[guess_row][guess_col] == "X":
			print("You guessed (" + str(guess_row) + ", " + str(guess_col) + ") already.")
		else:
			print("You missed my battleship!")
			board[guess_row][guess_col] = "X"

	# COUNT OUR TURNS, PRINT BOARD, AND LOOP BACK
	print("Guess - " + str(turn + 1))
	print_board(board)
	if turn == 3:
		print("""
   ____                         ___                 
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                    
""")

#EOF

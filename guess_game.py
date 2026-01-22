# Jongbeom Shim
# 2026/01/22
# v1.0

import random

# *f means foreground color, *b means background color
# for example, redf is "red foreground" and redb is "red background"
colors = {
	"redf" : "\033[31m",
	"greenf" : "\033[32m",
	"whitef" : "\033[37m",
	"redb" : "\033[41m",
	"greenb" : "\033[42m",
	"blueb" : "\033[44m"
}

mods = {
	"reset" : "\033[0m",
	"bold" : "\033[1m"
}

maxNum = 50 # Max range of random number
live = 5 # number of guesses
rand = random.randint(1, maxNum)

game_title = r"""
=======================================================
   ___                         ___                     
  / _ \_   _  ___  ___ ___    / _ \__ _ _ __ ___   ___ 
 / /_\/ | | |/ _ \/ __/ __|  / /_\/ _` | '_ ` _ \ / _ \
/ /_\\| |_| |  __/\__ \__ \ / /_\\ (_| | | | | | |  __/
\____/ \__,_|\___||___/___/ \____/\__,_|_| |_| |_|\___|

======================================================="""

game_instruction = f"""
============== {colors['redb']}INSTRUCTION!{colors['greenb']} ==============
Computer will choose a number between 1-{maxNum}.
You have {live} chances to guess the correct number.
Enter your guess and win the game!{mods['reset']}"""

def game_logic():
	global live
	
	while(True):
		user = 0
		
		# Input Handler
		while(True):
			try:
				user = int(input("guess the correct number: "))
				if(user <= 0):
					print(f"{colors['redb']}PLEASE ENTER A NUMBER BIGGER THAN ZERO{colors['blueb']}")
				elif(user > maxNum):
					print(f"{colors['redb']}PLEASE ENTER A NUMBER LOWER OR EQUAL TO {maxNum}{colors['blueb']}")
				else:
					break
			except ValueError:
				print(f"{colors['redb']}PLEASE ENTER A NUMBER{colors['blueb']}")
		
		# Game Logic
		if(rand == user):
			print(f"{colors['greenb']}============== YOU WON! =============={mods['reset']}\n")
			input("Enter to continue...")
			break
		elif(live <= 0):
			print(f"{colors['redb']}YOU LOST! The Answer Was {rand}{mods['reset']}\n")
			input("Enter to continue...")
			break
		else:
			print(f"{live} left: {colors['redf']}WRONG!{colors['whitef']} ", end="")
			print("UP!" if (rand > user) else "DOWN!")
			live -= 1

def game_menu():
	while(True):		
		print(f"{colors['greenf']}{mods['bold']}{game_title}{colors['whitef']}")
		print(f"{colors['greenb']}{mods['bold']}{game_instruction}")
		print(f"{colors['blueb']}{mods['bold']}")
		
		print("(1) Start\n(2) Exit")
		user = int(input("Select the number: "))
		if(user == 1):
			game_logic()
		elif(user == 2):
			break

game_menu()

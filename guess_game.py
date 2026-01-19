import random

# *f means foreground color, *b means background color
# for example, redf is "red foreground" and redb is "red background"
colors = {
	"redf" : "\033[31m",
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

# Instruction
print(f"{colors['greenb']}{mods['bold']}")
print(f"============== {colors['redf']}INSTRUCTION!{colors['whitef']} ==============\nComputer will choose a number between 1-{maxNum}.\nYou have {live} chances to guess the correct number.\nEnter your guess and win the game!{mods['reset']}")
print(f"{colors['blueb']}{mods['bold']}")

while(True):
	user = 0
	
	# Input Handler
	while(True):
		try:
			print("guess the correct number: ", end="")
			user = int(input())
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
		break
	elif(live <= 0):
		print(f"{colors['redb']}YOU LOST! The Answer Was {rand}{mods['reset']}\n")
		break
	else:
		print(f"{live} left: {colors['redf']}WRONG!{colors['whitef']} ", end="")
		print("UP!" if (rand > user) else "DOWN!")
		live -= 1

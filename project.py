import random

print("Welcome to my adventure game.")

game_start = input("\nWould you like to play? (y/n) ").lower()
usr_choice = ""
if game_start == 'y':
	usrname = input("What is your character name?: ")
	usrhealth = 20
	print("Hello", usrname, "your adventure begins in ")
	print("3 ", "2 ", "1 ")

	usr_choice = input("You wake up in the forest, in front of you is a forked path. Do you go left or right? (left/right): ")
	if usr_choice == 'left':
		usr_choice = input("You find a dagger with a letter in an unfamiliar language, do you pick up the dagger? (y/n): ").lower()
		if usr_choice == 'y':
			print("You have been imbued with the power of a Cursed Spirit LV.1, you continue on your path... ")
		elif usr_choice == 'n':
			print("You continue on your path... ")
	elif usr_choice == 'right':
		print("You run into a dire wolf, it attacks and runs off: -10 Health. ")
		usrhealth -= 10
		print("Character health:", usrhealth)
	else:
		print("Path does not exist... ")

else:
	print("Maybe next time... ")
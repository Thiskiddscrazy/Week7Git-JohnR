# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print() #This does not call to print the above intro: Write this instead:
    #displayIntro()

def chooseCave():
	#chooseCave is not defined since cave is empty; add an input like this:
    # cave = input(Which cave wil you go into: 1 or 2?" 

    cave = '' #Ok to earase this now -------------
	
	
	while cave != '1' and cave != '2':
		#Now put in the return function
	# (properly intented...return caves)

		print('Which cave will you go into? (1 or 2)')
		cave = input() #Okay to e       rase this now --------

	return caves 
##Put in the empty caves in a list like this-- chosenCave () then continue w/ function ;
# --chosenCave()
def checkCave(chosenCave):
	#There is not description below this or an actual definition. Insert a """ and write a description
	"""[Insert description for definition]"""
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' #We need parentheses to run this code like this:
		#print("Gobbles you down in one bite!")

#Theres no call to this function, so write this in the next line of code:

#checkCave(chosenCave)

playAgain = 'yes' #There is no input here, just what the term 'playAgain' means; write this: 
"""playAgain =input ("Would you like to play again? (yes or no)") [continue would be more clear to me,
 but let's go with their input] """
while playAgain = 'yes' or playAgain = 'y':   #Should be '==] like this:
#while playAgain == 'yes' or playAgain == 'y':

	displayIntro()
	caveNumber = choosecave() #ChosenCave, not 'choosecave' like this:
    #caveNumber - chosenCave() [Capitalization is impertive in coding]
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input() #No need for this, so erase this now -------
	if playAgain == "no":
		print("Thanks for planing")
#Should say thanks for "playing" [Spelling is important]
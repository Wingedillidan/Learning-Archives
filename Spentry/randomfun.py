import random, os
from sys import exit

def init():
	os.system('cls')
	prompt = '> '
	
	# generate a character
	# this is using everything I learned thus far... I haven't learned classes yet...
	# don't judge ;-;
	character = createchar(prompt)
	
	print "Do you test or not test?"
	print checkinput(prompt, ('test', 'not test'))

def createchar(prompt):
	
	# what is your name?
	print "So you're on your way to the lower chambers? What's your name stranger?"
	while True:
		result = {'name': raw_input(prompt).strip()}
		
		# check to make sure there is actually a name
		if len(result['name']) > 0:
			break
		else:
			print "Hey! Speak up! ... what's your name?"
	
	# setup stat generation
	print "Right, %s, let's take a look at your strengths and weaknesses..." % result['name']
	rerolls = 5
	types = ('health', 'combat', 'luck')
	
	# loop through each stat, generating a number 1-20 for them
	for stat in types:
		while True:
			result[stat] = int(random.randint(1,20))
			
			# the player gets n amount of rerolls in the event of bad luck
			if rerolls > 0:
				print "Your %s roll was %i, do you want to use a reroll? [%i reroll(s) left]" % (stat, result[stat], rerolls)
				
				if yesno(prompt) == False:
					break
				else:
					rerolls -= 1
			else:
				print "You rolled a %i for your %s." % (result[stat], stat)
				break
				
	# give the player a set amount of gold
	result['gold'] = 100
	print "\nYou planned well, you brought %i gold for this adventure.\n" % result['gold']
	
	return result
	
	
def checkinput(prompt, correct, error = "I didn't get that..."):
	# check for an accurate response
	while True:
		response = raw_input(prompt).lower()
		
		for i,answer in enumerate(correct, start = 1):
			if response == answer or response == str(i):
				return correct[i-1]


def yesno(prompt, error = "Was that a yes or no?"):
	# check for accurate yes or no response
	while True:
		response = raw_input(prompt).lower()
		
		if len(response) > 3:
			print error
		elif 'yes' in response or response == "y":
			return True
		elif 'no' in response or response == "n":
			return False
		else:
			print error

init()
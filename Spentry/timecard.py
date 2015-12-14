from datetime import datetime
from os.path import exists
from sys import exit
import json

def init():
	
	# TODO: Add configuration for timecard filename
	filename = "default_timecard.txt"
	
	# check if the timecard file exists
	# TODO: Make work.
	file = open(filename, 'a')
	
	# main options loop
	while True:
		print "Main Menu:\n[1] Create punch\n[2] Exit"
		
		# take user menu input
		response = raw_input("> ")
		
		if response == "1":
			punch(file)
			file.update()
		elif response == "2":
			exit(0)
			file.close()
		else:
			print "Sorry, please enter a number corresponding to the menu action."


def punch(file):
	
	# create a datetime object to add to the card
	timestamp = datetime.now()
	file.write(str(timestamp))


init()
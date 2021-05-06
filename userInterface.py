# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
# This file contains a general-purpose interface for user interaction

import keyboard
from console.utils import wait_key

# Things to have:
# Calendar of events
# Add/update/remove elements
# Search for elements

# These are commonly-used codes for terminal colors
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

artifact_fields = ['ID', 'Name', 'Type', 'Description', 'Age', 'ChainOCust', 'PlaceOfOrigin', 'ExhibitID', 'Value']
exhibit_fields = ['ID', 'Theme', 'MuseumLocID', 'LocInMuse', 'StartTime', 'EndTime']
museum_fields = ['ID', 'Name', 'Address']

# For proper searching we need to differentiate between chars/non-chars and ints/non-ints
non_char_fields = ['Age', 'Value', 'StartTime', 'EndTime']
int_fields = ['Age', 'Value']

# Instructions is a simple string that is printed before the options, as an introduction to what input is requested
# Options is a list of pairs. Each pair consists of a string prompt that will be rendered as an option for the user to
# select, and a function that will be executed if that option is selected. An option is selected by pressing the key for
# the first character in the option (e.g. press A to select "Add element")
def request_input(instructions, options):
	print(instructions)
	for prompt, _ in options:
		print(f"{COLOR_BLUE}" + prompt[0] + f"{COLOR_RESET}" + prompt[1:])
	while True: # Loop until a key is pressed that matches our prompt
		keypressed = wait_key()
		for prompt, func in options:
			if keypressed == prompt[0].lower():
				return func()

# Prompts the user to select a single field from the table, or choose all
# Table should be a string with one of the values: artifact, exhibit, or museum
# Returns the name of the field they chose
def select_field(instructions, table):
	fields = []
	if table.lower() == "artifact":
		fields = artifact_fields
	elif table.lower() == "exhibit":
		fields = exhibit_fields
	elif table.lower() == "museum":
		fields = museum_fields
	else:
		raise Exception("Table value must be one of: artifact, exhibit, museum")
	
	print(instructions)
	for field in fields:
		print(f"{COLOR_BLUE}" + field[0] + f"{COLOR_RESET}" + field[1:])
	while True:  # Loop until a key is pressed that matches our prompt
		wait_key()
		keypressed = keyboard.read_key()
		for field in fields:
			if keypressed == field[0].lower():
				return field

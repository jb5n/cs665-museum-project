# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
# This file contains all the functions for modifying the database: insert, update, and delete operations

import keyboard
import userInterface

def insert_disambiguation():
	def insert_artifact():
		...
	
	def insert_exhibit():
		...
	
	def insert_museum():
		...
	
	userInterface.RequestInput(
		"Select the type of element you want to insert by pressing the highlighted key:",
		[
			("Artifact", insert_artifact),
			("Exhibit", insert_exhibit),
			("Museum", insert_museum),
			("Quit", lambda: None)
		])

def modify_disambiguation():
	...

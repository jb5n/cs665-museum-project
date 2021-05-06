# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
# This file contains all the functions for modifying the database: insert, update, and delete operations

import dbConnector
import userInterface

def insert_database():
	table = userInterface.request_input(
		"Select the type of element you want to add by pressing the highlighted key:",
		[
			# ("W - All categories", lambda: "all"),
			("Artifact", lambda: "artifact"),
			("Exhibit", lambda: "exhibit"),
			("Museum", lambda: "museum"),
			("Quit", lambda: None)
		])
	if table is None:  # User selected the Quit option
		return

	fields = []
	if table.lower() == "artifact":
		fields = artifact_fields
	elif table.lower() == "exhibit":
		fields = exhibit_fields
	elif table.lower() == "museum":
		fields = museum_fields
	
	insert_values = []
	
	

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
			("Artifact", lambda: "artifact"),
			("Exhibit", lambda: "exhibit"),
			("Museum", lambda: "museumlocation"),
			("Quit", lambda: None)
		])
	if table is None:  # User selected the Quit option
		return

	fields = []
	if table.lower() == "artifact":
		fields = userInterface.artifact_fields
	elif table.lower() == "exhibit":
		fields = userInterface.exhibit_fields
	elif table.lower() == "museumlocation":
		fields = userInterface.museum_fields
	
	insert_values = []
	
	for field in fields:
		insert_values.append('"' + input(f"Input desired value for field {field}:\n> ") + '"')
	
	insert_string = ", ".join(insert_values) # Combine all values into one string
	try:
		dbConnector.db_cursor.execute(
			f"INSERT INTO {table} VALUES ({insert_string})")
		dbConnector.db_connection.commit()
	except Exception as e:
		print(f"Failed to insert data. Error: {e}")


def update_database():
	table = userInterface.request_input(
		"Select the type of element you want to update by pressing the highlighted key:",
		[
			("Artifact", lambda: "artifact"),
			("Exhibit", lambda: "exhibit"),
			("Museum", lambda: "museumlocation"),
			("Quit", lambda: None)
		])
	if table is None:  # User selected the Quit option
		return
	
	target_id = input(f"Enter the ID of the {table} you wish to modify:\n> ")

	field = userInterface.select_field(
            "Select the field you want to modify by pressing the highlighted key:", table)
	if field is None:  # User selected the Quit option
		return
	
	new_value = input(f"Enter the new value of {field}:\n> ")
	
	try:
		dbConnector.db_cursor.execute(
			f"UPDATE {table} SET {field}=\"{new_value}\" WHERE ID=\"{target_id}\"")
		dbConnector.db_connection.commit()
	except Exception as e:
		print(f"Failed to update data. Error: {e}")
		return
	print("Update Successful")
		

def delete_database():
	table = userInterface.request_input(
		"Select the type of element you want to delete by pressing the highlighted key:",
		[
			("Artifact", lambda: "artifact"),
			("Exhibit", lambda: "exhibit"),
			("Museum", lambda: "museumlocation"),
			("Quit", lambda: None)
		])
	if table is None:  # User selected the Quit option
		return

	target_id = input(f"Enter the ID of the {table} you wish to delete:\n> ")

	try:
		dbConnector.db_cursor.execute(f"DELETE FROM {table} WHERE ID=\"{target_id}\"")
		dbConnector.db_connection.commit()
	except Exception as e:
		print(f"Failed to delete field. Error: {e}")
		return
	print("Delete Successful")

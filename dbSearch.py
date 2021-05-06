# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
# This file contains all the functions for modifying the database: insert, update, and delete operations

import dbConnector
import userInterface

# Search for an artifact, exhibit, or museum in the database
def search_db():
	table = userInterface.request_input(
		"Select the type of element you want to search for by pressing the highlighted key:",
		[
			("Artifact", lambda: "artifact"),
			("Exhibit", lambda: "exhibit"),
			("Museum", lambda: "museumlocation"),
			("Quit", lambda: None)
		])
	if table is None: # User selected the Quit option
		return

	field = userInterface.select_field(
            "Select the field you want to search for by pressing the highlighted key:", table)
	if field is None:  # User selected the Quit option
		return
	
	query = input("Input your search query:\n> ")
	print(f"\nSearching for {field} in {table}")

	try:
		if field in userInterface.int_fields:
			dbConnector.db_cursor.execute(f"SELECT * FROM {table} WHERE {field}={query}")
		elif field in userInterface.non_char_fields:
			dbConnector.db_cursor.execute(
				f"SELECT * FROM {table} WHERE {field}=\"{query}\"")
		else:  # We can only use LIKE on char fields
			dbConnector.db_cursor.execute(
				f"SELECT * FROM {table} WHERE {field} LIKE \"%{query}%\"")
	except Exception as e:
		print(f"Search Failed. Error: {e}\n")
		return
	print(f"Search Results:\n{dbConnector.db_cursor.fetchall()}\n")
	
	
# View the available exhibits on a given day
def search_calendar():
	query = input("Input a date you would like to see the exhibits for:\n> ")
	try:
		dbConnector.db_cursor.execute(f"SELECT * FROM Exhibit WHERE StartTime <= '{query}' AND EndTime >= '{query}'")
	except Exception as e:
		print(f"Database search failed. Error: {e}\n")
		return
	print(f"The following exhibits will be available on {query}:\n{dbConnector.db_cursor.fetchall()}\n")
	

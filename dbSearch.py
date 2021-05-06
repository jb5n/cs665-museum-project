# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
# This file contains all the functions for modifying the database: insert, update, and delete operations

from dbConnector import db_cursor


def search_db():
	query = input("Input your search query:\n> ")
	# Surround the query in % so that we don't have to append them when passing the query to the database
	query_substr = "%" + query + "%"

	table = userInterface.request_input(
		"Select the type of element you want to search for by pressing the highlighted key:",
		[
			("W - All categories", lambda: "all"),
			("Artifact", lambda: "artifact"),
			("Exhibit", lambda: "exhibit"),
			("Museum", lambda: "museum"),
			("Quit", lambda: None)
		])
	if table is None: # User selected the Quit option
		return

	field = "all"	
	if table != "all":
		# If we are not searching all tables, prompt what field they specifically want to search
		field = userInterface.select_field(
			"Select the field you want to search for by pressing the highlighted key:", table)
		if field is None:  # User selected the Quit option
			return
	
	search_results = []
	
	if field == "all":
		if table == "all" or table == "artifact":
			search_results.append(db_cursor.execute(
				f"""SELECT * FROM Artifact WHERE
					ID={query} OR
					Name LIKE {query_substr} OR
					Type LIKE {query_substr} OR
					Description LIKE {query_substr} OR
					Age={query} OR
					ChainOCust LIKE {query_substr} OR
					PlaceOfOrigin LIKE {query_substr} PR
					ExhibitID={query} OR
					Value={query}"""
			))
		elif table == "all" or table == "exhibit":
			search_results.append(db_cursor.execute(
				f"""SELECT * FROM Exhibit WHERE
					ID={query} OR
					Theme LIKE {query_substr} OR
					MuseumLocID={query} OR
					LocInMuse LIKE {query_substr} OR
					StartTime={query} OR
					EndTime={query}"""
			))
		elif table == "all" or table == "museum":
			search_results.append(db_cursor.execute(
				f"""SELECT * FROM MuseumLocation WHERE
					ID={query} OR
					Name LIKE {query_substr} OR
					Address LIKE {query_substr}"""
			))
	else:
		...
	

# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
# This is the entry point for the program

import dbConnector
import dbModification
import dbSearch
from getpass import getpass
import sys
import userInterface

print("***MUSEUM ARTIFACT MANAGEMENT SYSTEM***")
hostname = input("Please input your MariaDB database hostname\n> ")
username = input("Please input your username\n> ")
password = getpass("Please input your password\n> ")

dbConnector.connect_to_database(username, password, hostname)

while True:
	userInterface.request_input(
            "Select an operation by pressing the highlighted key:",
            [
                ("Search for an artifact, exhibit, or museum", dbSearch.search_db),
       		   ("View the calendar of exhibits", dbModification.insert_disambiguation),
       		   ("Add element to database", dbModification.insert_disambiguation),
       		   ("Edit existing element in database",
       		    dbModification.insert_disambiguation),
       		   ("Delete element from the database",
       		    dbModification.insert_disambiguation),
       		   ("Quit", lambda: sys.exit(1))
            ])
	print("***MUSEUM ARTIFACT MANAGEMENT SYSTEM***")

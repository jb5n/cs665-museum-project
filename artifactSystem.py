# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
# This is the entry point for the program

from getpass import getpass

import dbConnector
import dbModification
import dbSearch
import userInterface

# Initial connection and setup
userInterface.print_header()
hostname = input("Please input your MariaDB database hostname\n> ")
username = input("Please input your username\n> ")
password = getpass("Please input your password\n> ")
dbConnector.connect_to_database(username, password, hostname)

# Loop until the user quits
while True:
	userInterface.request_input(
            "Select an operation by pressing the highlighted key:",
            [
                ("Search for an artifact, exhibit, or museum", dbSearch.search_db),
       		   ("View and search the calendar of exhibits", dbSearch.search_calendar),
       		   ("Add element to database", dbModification.insert_database),
       		   ("Edit existing element in database", dbModification.update_database),
       		   ("Delete element from the database", dbModification.delete_database),
       		   ("Quit", lambda: sys.exit(1))
            ])
	userInterface.print_header()

# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
import mariadb
import sys
from getpass import getpass
import keyboard
import userInterface
import dbModification
import dbSearch

print("***MUSEUM ARTIFACT MANAGEMENT SYSTEM***")
hostname = input("Please input your MariaDB database hostname\n> ")
username = input("Please input your username\n> ")
password = getpass("Please input your password\n> ")

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=username,
        password=password,
        host=hostname,
        port=3306,
        database="museumInventory"

    )
except mariadb.Error as e:
    print(f"Error connecting to database: {e}")
    sys.exit(1)

# Get Cursor
db_cursor = conn.cursor()

userInterface.request_input(
    "Select an operation by pressing the highlighted key:",
   	[
		   ("Search for an artifact, exhibit, or museum", dbSearch.search_db),
		   ("View the calendar of exhibits", dbModification.insert_disambiguation),
		   ("Add element to database", dbModification.insert_disambiguation),
		   ("Edit existing element in database", dbModification.insert_disambiguation),
		   ("Delete element from the database", dbModification.insert_disambiguation),
		   ("Quit", lambda: sys.exit(1))
	])

#while True:
#	print("Select an operation by pressing the highlighted key:")
#	print(f"{COLOR_BLUE}S{COLOR_RESET}earch for an artifact, exhibit, or museum")
#	print(f"{COLOR_BLUE}A{COLOR_RESET}dd element to database")
#	print(f"{COLOR_BLUE}E{COLOR_RESET}dit existing element in database")
#	print(f"{COLOR_BLUE}D{COLOR_RESET}elete element from the database")
#	print(f"{COLOR_BLUE}Q{COLOR_RESET}uit")
	
#	while True:
#		keypressed = keyboard.read_key()
#		if keypressed == "s":
			

# Things to have:
# Calendar of events
# Add/update/remove elements
# Search for elements

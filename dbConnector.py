# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
import mariadb
import sys

db_connection = None
db_cursor = None

def connect_to_database(username, password, hostname):
	# Connect to MariaDB Platform
	global db_cursor
	global db_connection
	try:
		db_connection = mariadb.connect(
			user=username,
			password=password,
			host=hostname,
			port=3306,
			database="museuminventory"
		)
	except mariadb.Error as e:
		print(f"Error connecting to database: {e}")
		sys.exit(1)
	db_cursor = db_connection.cursor()

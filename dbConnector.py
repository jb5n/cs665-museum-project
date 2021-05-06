# CS 665 Group Project
# Museum Artifact Management System
# Justin Bostian, Bailey Kippenberger
import mariadb
import sys

db_cursor = None

def connect_to_database(username, password, hostname):
	# Connect to MariaDB Platform
	try:
		conn = mariadb.connect(
			user=username,
			password=password,
			host=hostname,
			port=3306,
			database="museuminventory"
		)
	except mariadb.Error as e:
		print(f"Error connecting to database: {e}")
		sys.exit(1)
	global db_cursor
	db_cursor = conn.cursor()

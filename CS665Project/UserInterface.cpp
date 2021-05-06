#include <iostream>
#include <string>
#include "DatabaseConnector.h"

using namespace std;

DatabaseConnector* db;

string getInput(string prompt) {
	cout << prompt << "\n> ";
	string input = "";
	cin >> input;
	return input;
}

void Connect() {
	// First we must connect to the database
	cout << "DATABASE CONNECTION SETUP\n";
	string hostname = getInput("Please input the database hostname");
	string username = getInput("Please input the database username");
	// It's a bad practice to have the user enter their password without masking
	// If this were a real product we would use a library to mask the password
	string password = getInput("Please input the database password");

	db = new DatabaseConnector(hostname, username, password);
}

int main() {
	Connect();

	return 0;

}
#include "DatabaseConnector.h"

DatabaseConnector::DatabaseConnector(string hostname, string username, string password)
{
    // Initialize constants
    MY_HOSTNAME = hostname.c_str();
    MY_DATABASE = "mysql";
    MY_USERNAME = username.c_str();
    MY_PASSWORD = password.c_str();
    MY_SOCKET = NULL;

    try {
        if (!mysql_real_connect(
            conn,
            MY_HOSTNAME, MY_USERNAME,
            MY_PASSWORD, MY_DATABASE,
            MY_PORT_NO, MY_SOCKET, MY_OPT)) {
            cerr << mysql_error(conn) << endl;
            exit(1);
        }
    }
    catch (...) {
        exit(1);
    }
}

bool DatabaseConnector::TryConnect() {
    conn = mysql_init(NULL);

    // Establish a MySQL connection
    if (!mysql_real_connect(
        conn,
        MY_HOSTNAME, MY_USERNAME,
        MY_PASSWORD, MY_DATABASE,
        MY_PORT_NO, MY_SOCKET, MY_OPT)) {
        cerr << mysql_error(conn) << endl;
        return false;
    }
    return true;
}
// Much of this code was taken and reworked from https://gist.github.com/komasaru/c9c6c03bda4629283808

#pragma once

#include <iostream>
#include <mysql/mysql.h>  // require libmysqlclient-dev
#include <string>

using namespace std;

class DatabaseConnector
{
    const char* MY_HOSTNAME;
    const char* MY_DATABASE;
    const char* MY_USERNAME;
    const char* MY_PASSWORD;
    const char* MY_SOCKET;
    enum {
        MY_PORT_NO = 3306,
        MY_OPT = 0
    };
    MYSQL* conn;
    MYSQL_RES* res;
    MYSQL_ROW row;

public:
    DatabaseConnector(string hostname, string username, string password);
    bool TryConnect();
};

/*
 * Main Process
 *
bool Proc::execMain()
{
    try {
        // Format a MySQL object
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

        // Execute a sql statement
        if (mysql_query(conn, "SHOW TABLES")) {
            cerr << mysql_error(conn) << endl;
            return false;
        }

        // Get a result set
        res = mysql_use_result(conn);

        // Fetch a result set
        cout << "* MySQL - SHOW TABLES in `"
            << MY_DATABASE << "`" << endl;
        while ((row = mysql_fetch_row(res)) != NULL)
            cout << row[0] << endl;

        // Release memories
        mysql_free_result(res);

        // Close a MySQL connection
        mysql_close(conn);
    }
    catch (char* e) {
        cerr << "[EXCEPTION] " << e << endl;
        return false;
    }
    return true;
}*/
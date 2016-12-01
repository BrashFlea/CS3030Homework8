#!/usr/bin/env python3
import sys
from dbconfig import read_db_config
import mysql.connector
from mysql.connector import Error, MySQLConnection


def connect():
    """
    Connect to SQL Database with config file
    """
    db_config = read_db_config()
    
    try:
        print("Connecting to MySQL database..")
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print("Connection Established!")
        else:
            print("Connection Failed")

        # Select some data
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer")
        # Store it in a list
        contents = list(cursor.fetchall())
        if contents is not None:
            return contents

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        print("Connection Close")


# Main function
def main():
    """
    Test Function.
    """
    connect()
    pass

if __name__ == "__main__":
    main()
    exit(0)

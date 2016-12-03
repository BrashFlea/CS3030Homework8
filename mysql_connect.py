#!/usr/bin/env python3
import sys
from dbconfig import read_db_config
import mysql.connector
from mysql.connector import Error, MySQLConnection


def connect(bDate, eDate):
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

        # Select data using bDate and eDate as delimiters
        cursor = conn.cursor()
        cursor.execute("SELECT t.trans_id, DATE_FORMAT(t.trans_date, \"%Y%m%d%h%i\") as trans_date, SUBSTRING(t.card_num, 9,14) AS card_num, tl.qty, tl.amt, p.prod_desc, t.total FROM products p, trans t, trans_line tl WHERE p.prod_num = tl.prod_num AND tl.trans_id = t.trans_id AND t.trans_date BETWEEN %s AND %s ORDER BY t.trans_date", (bDate, eDate))
        # Store it in a list
        contents = list(cursor.fetchall())

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        print("Connection Close")
        if contents is not None:
            return contents


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

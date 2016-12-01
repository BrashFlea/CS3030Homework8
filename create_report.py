#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ÃÂÃÂÃÂÃÂ© 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys
from configparser import ConfigParser
from dbconfig import read_db_config
from mysql_connect import connect
from pprint import pprint as pp


def convDate(beg_date, end_date):
    """
    Takes beginning date and end date as parameters to query the database.
    Converts the inputs to proper format YYYY-MM-DD hh:mm
    Args:
        beg_date: date in YYYYMMDD format
        end_date: date in YYYYMMDD format
    Returns:
    """
    db = read_db_config()

    if(len(str(beg_date)) != 8 or len(str(end_date)) != 8):
        print("Improper date format. Please use the format <YYYYMMDD>")
        exit(-1)

    #Convert to list to add elements
    convB_date = list(str(beg_date))
    convE_date = list(str(end_date))
    #Add dashes, whitespace, and time
    #Year
    convB_date.insert(4, "-")
    convE_date.insert(4, "-")
    #Month
    convB_date.insert(7, "-")
    convE_date.insert(7, "-")
    #Time (whitespace)
    convB_date.insert(11, " ")
    convE_date.insert(11, " ")
    #Time (value)
    convB_date.insert(12, "00:00")
    convE_date.insert(12, "23:59")
    
    #Assign to new variables for database query
    bDate = "".join(convB_date)
    eDate = "".join(convE_date)

    #Connect to database and retrieve contents for manipulation
    contents = connect(bDate, eDate)
    print(contents)
    

# Main function
def main(beg_date, end_date):
    convDate(beg_date, end_date)
    return


if __name__ == "__main__":
    # Call Main
    beg_date = 20001018
    end_date = 20161231
    main(beg_date, end_date)

    exit(0)


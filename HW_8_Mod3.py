#!/usr/bin/python3
import time
import os, sys
import datetime
from optparse import OptionParser
from datetime import datetime
From mysql.connector import (connection) 
#from mysql.connector import error
#import MySQLdb.connector


parser = OptionParser()

if sys.argv[1] == "-u" and sys.argv[3] == "-d" and  sys.argv[5] == "-p" and sys.argv[7] == "-b" and sys.argv[9] == "-b" :


parser.add_option("-u", "--username", type="string",
                    help="insert the the",
            dest="user")


parser.add_option("-d", "--databaseName", type="string",
                    help="this is the name of database",
            dest="data")


parser.add_option("-p", "--password", type="string",
                    help="this is the login password",
            dest="passw")


parser.add_option("-e", "--enddate", type="string",
                    help="End Date with the following format: YYYYMMDD ",
            dest="Enddate")


parser.add_option("-b", "--begindate", type="string",
                     help="Begin Date with the following format: YYYYMMDD ",
            dest="begin")


(options, args) = parser.parse_args()

def beginFormatted():

    date = (options.begin + " 00:00:00")


    datetimeobject = datetime.strptime(date,'%Y%m%d %H:%M:%S')

    print(datetimeobject)



def endFormatted():
     date2 = (options.Enddate + " 23:59:00")

     datetimeobject2 = datetime.strptime(date2, '%Y%m%d %H:%M:%S')

     print(datetimeobject2)



def sqlquary():
    mysql -u (options.user) -p (options.passw) -d (option.data)



def main():
    beginFormatted()

    endFormatted()

    sqlquary()

#def dateChange():


#testr = SimpleDateFormat("yyyy-MM-dd hh:mm:ss").format(date);


main()








#!/bin/bash - 
#===============================================================================
#
#          FILE: run_report.sh
# 
#         USAGE: ./run_report.sh 
# 
#   DESCRIPTION: 
# 
#        AUTHOR: Bryson Oakley (), brysonoakley@mail.weber.edu
#       CREATED: 12/03/2016 05:19
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

showHelp() {
	echo "This file will run the create_report.py file with the specified dates and ftp the results to the FTP server using the supplied credentials. Errors will be reported to the email"
	echo "Usage: $0 -f <beginDate> -t <endDate> -e <email> -u <user> -p <password>"

	exit -5
}


while getopts ":f:t:e:u:p:" opt
do
	case $opt in
		f) begin=$OPTARG
			;;
		t) end=$OPTARG
			;;
		e) email=$OPTARG
			;;
		u) user=$OPTARG
			;;
		p) password=$OPTARG
			;;
		h) showHelp
			;;
		\?) echo "Unknown arg: $opt"
			showHelp
			;;
	esac
done

if [[ $begin == "" || $end == "" || $email == "" || $user == "" || $password == "" ]]
then
	showHelp
fi

python3 create_report.py $begin $end

if [[ $? -eq 0 ]]
then
	
fi

exit 0


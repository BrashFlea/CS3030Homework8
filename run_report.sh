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
		\?) showHelp
			;;
	esac
done

if [[ $begin == "" || $end == "" || $email == "" || $user == "" || $password == "" ]]
then
	showHelp
fi

fileDate=`date +%Y_%m_%d-%H:%m`
file="report-$fileDate.txt"

python3 create_report.py $begin $end > $file
result=$?

sed -i '1,3d' $file

if [[ $result -eq 255 ]] # For some reaseon, if python exits with a negative number, it is just taken away from 256
then
	echo "Exited with -1. Sending an email..."
	mail -s "The create_report program exited with code -1" -r "run_report_script@yourscripts.net" $email << EOF
	The create_report could not run due to invalid date params. Please review it's documentation.
EOF
elif [[ $result -eq 254 ]]
then
	echo "Exited with -2. Sending an email..."
	mail -s "The create_report program exited with code -2" -r "run_report_script@yourscripts.net" $email << EOF
	The create_report program ran, but no transactions were found within the specified date range
EOF
else
	echo "All good. Zipping and sending now"
	zipFile="report-$fileDate.zip"
	zip $zipFile $file
	
	ftpAddress=137.190.19.104
	echo "Attempting to ftp..."
	ftp -inv $ftpAddress << COMMS
	user $user $password
	put $zipFile
	bye
COMMS
	rm $zipFile

	mail -s "run_report.sh ran successfully to $ftpaddress" -r "run_report_script@yourscripts.net" $email << EOF
	Successfully created a transaction report from $begin to $end
EOF
fi

rm $file 

exit 0


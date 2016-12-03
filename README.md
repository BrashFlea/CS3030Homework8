#CS3030Homework8

Jonathan Mirabile

Burak Deniz

Bryson Oakley

Python/MySQL/Bash report generator


**Module 1** - config.ini file containing database credentials. Obviously this has been omitted from the repository for security reasons. 

The required format for the config.ini file is as follows:

[mysql]

host = localhost

database = DATABASE NAME

user = USERNAME

password = PASSWORD

The config.ini file is parsed by the included dbconfig.py module and passed to mysql\_connect.py for use in Module 2 


**Module 2** - create\_report.py 

Requires two arguments (*beg\_date*, *end\_date*) in the format &lt;YYYYMMDD&gt;

Connects to the database using config.ini parsed by dbconfig.py and generates a fixed length report using *beg\_date* and *end\_date* as delimiters for the data.

Exit codes:

**-1:** Improper date format

**-2:** No data for given date range

**0:** Successful execution


**Script 1** - run\_report.sh

Shell wrapper script that runs create\_report.py, generates a zipped copy of the report, uploads it to the given FTP server, and emails the status of the FTP upload. 

Required paramters:

**-f** &lt;BegDate&gt;

**-t** &lt;EndDate&gt;

**-e** &lt;email&gt;

**-u** &lt;user&gt;

**-p** &lt;passwd&gt;

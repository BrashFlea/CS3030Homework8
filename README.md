#CS3030Homework8

Jonathan Mirabile

Burak Deniz

Bryson Oakley

Python/MySQL/Bash report generator

**Module 1** - config.ini file containing database credentials. Obviously this has been omitted from the repository for security reasons. 

The requires format for the config.ini file is as follows:

[mysql]

host = localhost

database = DATABASE NAME

user = USERNAME

password = PASSWORD

The config.ini file is parsed by the included dbconfig.py module and passed to mysql\_connect.py for use in Module 2 

**Module 2** - create\_report 

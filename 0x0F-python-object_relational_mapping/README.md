# Python - Object-relational mapping
* Python
* OOP
* SQL
* MySQL
* ORM
* SQLAlchemy

This project links Databases and Python, using:
* MySQLdb to connect to a MySQL database and execute your SQL queries.
* SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

* NO more SQL queries.!

## Concepts
* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Files will be executed with MySQLdb version 2.0.x
* Files will be executed with SQLAlchemy version 1.4.x
* Code uses the pycodestyle (version 2.8.*)
* The length of your files will be tested using wc

## More Info
### Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

* $ sudo apt-get install python3.8-venv
* $ python3 -m venv venv
* $ source venv/bin/activate
### Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed:
* $ sudo apt-get install python3-dev
* $ sudo apt-get install libmysqlclient-dev
* $ sudo apt-get install zlib1g-dev
* $ sudo pip3 install mysqlclient
...
* $ python3
* >>> import MySQLdb
*>>> MySQLdb.version_info 
* ( 2, 0, 3, 'final', 0)
###Install SQLAlchemy module version 1.4.x
* $ sudo pip3 install SQLAlchemy
* ...
* $ python3
* >>> import sqlalchemy
* >>> sqlalchemy.__version__ 
* '1.4.22'



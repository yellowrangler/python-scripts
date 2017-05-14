#!/usr/bin/python
import MySQLdb

import pdb


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="tarryc",         # your username
                     passwd="tarryc",  # your password
                     db="ddd")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM membertbl")

# print all the first cell of all the rows
for row in cur.fetchall():
	# pdb.set_trace()

	id = row[0]
	name = row[1]
	myrow = 'Hello'
	myrow = 'ID:'+str(id)+' Name:'+name
	print myrow

db.close()
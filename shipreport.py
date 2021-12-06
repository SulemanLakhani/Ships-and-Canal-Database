# shipreport.py
# Created by: Suleman Lakhani
# Date: 11-29-2021
import sys
import getpass
from psycopg2 import connect

# We are going to connect to the database as the user running
# the python program.
dbuser = getpass.getuser()

# Prompt and extract the password used to connect to the db.
dbpass = getpass.getpass()

# Open a connection to the database.
connStr = "host=pascal.rmc.edu dbname=group4 user=%s password=%s" % (dbuser, dbpass) 
conn = connect( connStr )
  
# Create a database cursor.
dbcursor = conn.cursor()

# manipulate the query as required

# Query the database for the list of ships.

#Ship id ship_name ship_type ship_weight captain_name company_name
dbcursor.execute("SET search_path TO final")

dbcursor.execute("CREATE TEMP TABLE t1 AS SELECT * FROM ships NATURAL JOIN operate")

dbcursor.execute("CREATE TEMP TABLE t2 AS SELECT captain_id, captain_name, comp_id, comp_name FROM captains NATURAL JOIN companies")

dbcursor.execute("SELECT ship_id, ship_name, ship_type, ship_weight, captain_name, comp_name FROM t1 NATURAL JOIN t2")

# header
txt = "Ship Report"
print(txt.center(93))

print("")

print("SHIP ID#  ", "SHIP NAME"," "*5,"SHIP TYPE", " "*7, "SHIP WEIGHT  ", "CAPTAIN NAME      ","COMPANY NAME")

print("-"*8, " ", "-"*9, " "*5, "-"*9, " "*7, "-"*11, " ","-"*12, " "*5 , "-"*12)

# Use the tuples.
recordList = dbcursor.fetchall()

#print(recordList)

#prints all tuples
for record in recordList :
	print("%8d   %-15s %-18s %10.2f   %-18s %-15s" % record)

print("-"*93)

#calculates store count of ships from ships table
dbcursor.execute("SELECT count(*) from ships")

# Use the tuples.
numofShips = dbcursor.fetchall()

#print(numofShips)
print("Number of Ships: %d" % numofShips[0])

# Close the connection to the database.
conn.close()
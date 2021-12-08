# shipstravelschedule.py
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

def printShips() :
	dbcursor.execute("SELECT ship_id, ship_name FROM ships")
	
	print("SHIP ID#", "SHIP NAME")
	print("-"*8, "-"*9,)
	
	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#prints all tuples
	for record in recordList :
		print("%8d %-16s" % record)
	
	print("-"*20)

def shipSelected(choice) :
	
	# header
	txt = "Ship Travel Schedule"
	print(txt.center(48))
	print("")
	
	dbcursor.execute("SELECT ship_name FROM ships WHERE ship_id = %d" % choice)
	
	recordList = dbcursor.fetchall()
	for record in recordList :
		print("%-16s".center(48) % record)
	
	print("")
	
	dbcursor.execute("CREATE TEMP TABLE t1 AS SELECT shipment_date, sum(num_containers) FROM hold WHERE ship_id = %d GROUP BY shipment_date" % choice)
		
	dbcursor.execute("CREATE TEMP TABLE t2 AS SELECT passage_date, shipment_date, canal_name FROM passage NATURAL JOIN canals WHERE ship_id = %d" % choice)

	#passage_date shipment_date num_containers canal_name
	dbcursor.execute("SELECT passage_date, shipment_date, sum as total_containers, canal_name FROM t1 NATURAL JOIN t2")
	
	print("PASSAGE DATE","SHIPMENT DATE","TOTAL CONTAINERS","CANAL NAME")
	print("-"*12, "-"*13,"-"*16, "-"*10)
	
	# Use the tuples.
	recordList = dbcursor.fetchall()
		
	#prints all tuples
	for record in recordList :
		print("%12s %13s %12d     %-16s" % record)
	
	print("-"*55)
	
# Query the database.
dbcursor.execute("SET search_path TO final")
	
printShips()

choice = int(input("Enter the ship_id for the Ship Schedule: "))
print("")
shipSelected(choice)

# Close the connection to the database.
conn.close()
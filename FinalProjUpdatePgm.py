# sample2.py

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

# What info would you like to update? 
print ("What would you like to update?")
print()
#print ("canal_name, passage_date, comp_name, headquarters, ship_name, cargo_type, cargo_value, captain_name")
print ("  [1] canals")
print ("  [2] companies")
print ("  [3] captains")
print ("  [4] ships")
print ("  [5] cargo types")
print ("  [6] ship cargo hold data")
print ("  [7] captain - ship assignments")
print ("  [8] canal passage records")
print()
#print ("Select and Enter the number for the information/data you would like to update:")

choice = int(input("Select and Enter the number for the information/data you would like to update: "))

# This function makes changes to the attributes of the canals table.
def showCanals() :

	dbcursor.execute("SELECT * FROM final.canals")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d   %-35s   %-10s   %-2s %-10s" % record)
		
def showCompanies() :
	print("Selected Option [2] 'companies'")
	
	dbcursor.execute("SELECT * FROM final.companies")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d   %-35s   %-10s  %-10s" % record)

def showCaptains() :
	print("Selected Option [3] 'Captains'")

	dbcursor.execute("SELECT * FROM final.captains")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d   %-50s" % record)

def showShips() :
	print("Selected Option [4] 'ships'")
	
	dbcursor.execute("SELECT * FROM final.ships")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d  %-35s  %-20s  %-10f  %-6d" % record)

def showCargoType() :
	print("Selected Option [5] 'cargo types'")
	
	dbcursor.execute("SELECT * FROM final.cargo")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d   %-35s  %-10d %-10f" % record)

def showHold() :
	print("Selected Option [6] 'ship cargo hold data")
	
	dbcursor.execute("SELECT * FROM final.hold")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d  %-6d  %-6s" % record)
	
def showShipAssignments() :
	print("Selected Option [7] 'captain - ship assignments'")

	dbcursor.execute("SELECT * FROM final.operate")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d   %-6d" % record)

def showPassage_Records() :
	print("Selected Option [8] 'canal passage records'")

	dbcursor.execute("SELECT * FROM final.passage")

	# Use the tuples.
	recordList = dbcursor.fetchall()
	
	#print(recordList)
	for record in recordList :
		print("%6d  %-6d  %-10s" % record)

if choice == 1 :
	showCanals()
elif choice == 2 :
	showCompanies()
elif choice == 3 :
	showCaptains()
elif choice == 4 :
	showShips()
elif choice == 5 :
	showCargoType()
elif choice == 6 :
	showHold()
elif choice == 7 :
	showShipAssignments()
elif choice == 8 :
	showPassage_Records()

# Close the connection to the database.
conn.close()

# group4_add.py
# Created by: Group 4

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



# Which table would you like to add data to? 
# Canal, passage, passage_entries, companies, ships, cargo, hold, operate, and captains.

print ("Tables in Database: ")
print ("canals, ships, companies, cargo, captains, passage, passage_entries, hold, operate")
tableChoice = input("Enter the table you would like to add data to: ")


 # This function adds data to the attributes of the canals table.
def addToCanals() :
	print("Adding to 'canals' table")
	
	 # retrieve attribute data from the user
	canal_id = int(input("Enter the canal_id for this canal: "))
	canal_name = input("Enter the canal_name for this canal: ")
	city = input("Enter the city where this canal is located: ")
	country = input("Enter the country where this canal is located: ")
	print("Enter 'state' if the canal is owned by a government OR 'private' if the canal is privately owned.")
	state_or_private = input("Enter 'state' or 'private': ")

	 # complete the add command.
	dbcursor.execute("INSERT INTO final.canals (canal_id, canal_name, city, country, state_or_private) \
		VALUES ( %d, '%s', '%s', '%s', '%s' )" % (canal_id, canal_name, city, country, state_or_private))
	
	conn.commit()

 # This function adds data to the ships table.
def addToShips() :
	print("Adding to 'ships' table")
	
	ship_id = int(input("Enter the ship_id: "))
	ship_name = input("Enter the ship_name: ")
	ship_type = input("Enter the ship_type: ")
	ship_weight = int(input("Enter the ship_weight (in tons): "))
	comp_id = input("Enter the company that owns this ship: ")
	
	dbcursor.execute("INSERT INTO final.ships (ship_id, ship_name, ship_type, ship_weight, comp_id) \
		VALUES ( %d, '%s', '%s', '%f', '%d' ) " % (ship_id, ship_name, ship_type, ship_weight, comp_id))
	
	conn.committ()
	
def addToCompanies() :
	print("Adding to 'companies' table")
def addToCargo() :
	print("Adding to 'cargo' table")
def addToCaptains() :
	print("Adding to 'captains' table")
def addToPassage() :
	print("Adding to 'passage' table")
def addToPassage_Entries() :
	print("Adding to 'passage_entries' table")
def addToHold() :
	print("Adding to 'hold' table")
def addToOperate() :
	print("Adding to 'operate' table")
	
	
	
	
 # Function Calls	
if tableChoice == "canals" :
	addToCanals()
elif tableChoice == "ships" :
	addToShips()
elif tableChoice == "companies" :
	addToCompanies()
elif tableChoice == "cargo" :
	addToCargo()
elif tableChoice == "captains" :
	addToCaptains()
elif tableChoice == "passage" :
	addToPassage()
elif tableChoice == "passage_entries" :
	addToPassage_Entries()
elif tableChoice == "hold" :
	addToHold()
elif tableChoice == "operate" :
	addToOperate()
	
	
	


# Close the connection to the database.
conn.close()
	
	
	
	
	
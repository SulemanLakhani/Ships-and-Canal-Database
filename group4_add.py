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
print ("Canals, Ships, Companies, Cargo, Captains, Passage, Passage_Entries, Hold, Operate")
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

	dbcursor.execute("SELECT * FROM final.canals")
	
	# Use the tuples.
	recordList = dbcursor.fetchall()
	print(recordList)
	
	for record in recordList :
		print("%4d   %-35s   %-2s" % record)
	
	 # complete the add command.
	dbcursor.execute("INSERT INTO final.canals (canal_id, canal_name, city, country, state_or_private) \
		VALUES ( %d, '%s', '%s', '%s', '%s' )" % (canal_id, canal_name, city, country, state_or_private))
	
	
	#sql = "INSERT INTO canals (canal_id, canal_name, city, country, state_or_private) VALUES ( %d, %s, %s, %s, %s )"
	#val = (canal_id, canal_name, city, country, state_or_private)
	
	#dbcursor.execute(sql, val)
	
	
	
def addToShips() :
	print("Adding to 'Ships' table")
def addToCompanies() :
	print("Adding to 'Companies' table")
def addToCargo() :
	print("Adding to 'Cargo' table")
def addToCaptains() :
	print("Adding to 'Captains' table")
def addToPassage() :
	print("Adding to 'Passage' table")
def addToPassage_Entries() :
	print("Adding to 'Passage_Entries' table")
def addToHold() :
	print("Adding to 'Hold' table")
def addToOperate() :
	print("Adding to 'Operate' table")
	
	
	
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
	
	
	
	
	
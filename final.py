# cs236
# Created by Parker Collins, Ryan Mero, and Suleman Lakhani
# report for the final project
# Total weight and value moving through a specific canal 

# imports 
import getpass
from psycopg2 import connect
import sys

# Logs into the database 
dbuser = getpass.getuser()
dbpass = getpass.getpass()
connStr = ("host=pascal.rmc.edu dbname=group4 user=%s password=%s" % (dbuser, dbpass))
conn = connect(connStr) 
dbcursor = conn.cursor()



def totalFunction() :
       
    # create temp tables 
    
    dbcursor.execute("Set search_path to final")
    
    dbcursor.execute("CREATE TEMP TABLE t1 as SELECT ship_id, ship_name, ship_weight FROM ships group by ship_id")
    
    
    dbcursor.execute("CREATE TEMP TABLE t2 as SELECT ship_id, ship_name, sum(cont_weight * num_containers) as total_cont_weight, shipment_date FROM t1 NATURAL JOIN hold")
    

    dbcursor.execute("Select ship_id, ship_name, ship_weight, num_containers, cont_weight, value, sum(ship_weight + (cont_weight * num_containers)) AS weight From t1 natural join t2")
    
    recordList = dbcursor.fetchall() 
    
    
	# print out the formatted version of the report	
    print("TOTAL WEIGHT AND VALUE THROUGH PANAMA CANAL")
    print("                                    2011-10-13                               ")
    print()
	
    print("SHIP#  SHIP-NAME SHIP_WEIGHT NUM_CONTAINERS CONT_WEIGHT VALUE  TOTAL_WEIGHT")
    print("-----  --------- ----------- -------------- ------------ -----  ------------")

	# select the records to be displayed
    for record in recordList :
	    print("%5d    %-10d   %-5.2f  %-4d   %-5.2f  %-5d   %-6.2f" % record)
		
    print("----------------------------------------------------------------------------")
	
	# print out the total weight and values
    total_weight = dbcursor.execute("Select sum(weight) from t1")
	
    total_value = dbcursor.execute("Select sum(value) from t1")
	
    print("Total WEIGHT: %d" % total_weight)
    print("Total VALUE:  %d" % total_value)

totalFunction()

conn.close()

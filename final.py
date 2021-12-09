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
    
    dbcursor.execute("Create temp table t1 as select ship_id, shipment_date, sum(num_containers) as total_num_cont, sum(cont_weight) as total_cont_weight, sum(value * num_containers) as total_value from cargo natural join hold group by shipment_date, ship_id")
    
    
    dbcursor.execute("select ship_id, ship_weight, shipment_date, total_num_cont, total_cont_weight, total_value from t1 natural join ships")
    

    dbcursor.execute("select ship_id, shipment_date, sum(ship_weight + (total_num_cont * total_cont_weight)) as total_weight, total_value from t1 natural join ships group by ship_id, shipment_date, total_value;")
    recordList = dbcursor.fetchall() 
    
    
	# print out the formatted version of the report	
    print("           TOTAL WEIGHT AND VALUE THROUGH PANAMA CANAL")
    print("                         2011-10-13                              ")
    print()
	
    print("SHIP#   SHIPMENT_DATE TOTAL_WEIGHT TOTAL VALUE")
    print("---------------------------------------------------------")

	# select the records to be displayed
    for record in recordList :
	    print("%5d   %10s  %-8d %-8d" % record)
		
    print("-----------------------------------------------------")
	
	# print out the total weight and values
    dbcursor.execute("create temp table t3 as select ship_id, shipment_date, sum(ship_weight + (total_num_cont * total_cont_weight)) as total_weight, total_value from t1 natural join ships group by ship_id, shipment_date, total_value;")
    
    dbcursor.execute("Select sum(total_weight) from t3")
    
    total_weight = dbcursor.fetchall()
	
    dbcursor.execute("Select sum(total_value) from t3")
    
    total_value = dbcursor.fetchall()
	
    print("Total WEIGHT: %d" % total_weight[0])
    print("Total VALUE:  %d" % total_value[0])

totalFunction()

conn.close()
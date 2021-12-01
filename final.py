# cs236
# Created by Parker Collins, Ryan Mero, and Suleman Lakhani
# report for the final project
# Total weight and value moving through a specific canal 

# imports 
import getpass
from psycopg2 import connect
import sys

def main() :
# Logs into the database 
    dbuser = getpass.getuser()
    dbpass = getpass.getpass()
    connStr = ("host=pascal.rmc.edu dbname=group4 user=%s password=%s" % \
                        (dbuser, dbpass))
    conn = connect(connStr) 
    dbcursor = conn.cursor()

# Functions to return the invoice
    invoiceNum = getArgs() 
    qResult = select(dbcursor, invoiceNum) 

# Close connection
    conn.close() 
    
# Gets the invoice number as an argument
def getArgs() :
    invoiceNum = 0
    if (len(sys.argv) > 0) : 
        for i in range(1,len(sys.argv)) :
            invoiceNum =  int(sys.argv[i])
# return arg
            return invoiceNum
    else :
        return

# get select statements to create the information 
def select(dbcursor, invoiceNum) :
# Create temp tables
    dbcursor.execute("""
                       CREATE TEMP TABLE table1 AS
                       SELECT *
                       FROM hold
                       NATURAL JOIN ships;
                     """)
# Create another table 
    dbcursor.execute("""
                       CREATE TEMP TABLE table2 AS
                       SELECT *
                       FROM cargo 
                       NATURAL JOIN canals;
                     """)
# Combine the two temp tables to get the weight
    dbcursor.execute("""
                       CREATE TEMP TABLE finalTable AS
                       SELECT ship_id, ship_weight, cargo_id, num_containers,
                       (ship_weight + (cont_weight * num_containers)) AS "weight"
                       FROM table1 NATURAL JOIN table2;
                     """)
    
    
# Combine tables to get the total value
    dbcursor.execute("""
                       CREATE TEMP TABLE finalTable AS
                       SELECT ship_id, ship_weight, cargo_id, num_containers,
                       (value * num_containers) AS "total_value"
                       FROM table1 NATURAL JOIN table2;
                     """)
# use the invoice num argument 
    dbcursor.execute("""
                       SELECT ship_id, date
                       FROM finalTable WHERE canal_id = %d;
                     """ % invoiceNum)

# obtain the records
    records = dbcursor.fetchone()
    shipID = records[0]
    canalID = records[1]
    date = records[3]

    dbcursor.execute("""
    	               SELECT SUM(weight) FROM finalTable WHERE canal_id = %d;
    	             """ % invoiceNum)
    records = dbcursor.fetchone()
# set the total
    total = records[0]

    dbcursor.execute("""
                       SELECT ship_id, ship_weight, cont_weight, num_containers, weight, total_value
                       FROM finalTable WHERE canal_id = %d;
                     """ % invoiceNum)

    records = dbcursor.fetchall()
# Print 
    printFormat(records, invoiceNum, shipID, state_or_private, date, total)

def printFormat(result, invoiceNum, shipID, state_or_private, date, total):

# print out the formatted version of the report	
	print("   TOTAL WEIGHT AND VALUE THROUGH CANALS          ")

	print(" 	  Invoice #%d\n" % invoiceNum)
    print("        #%3d - %-20s" % (canalID))
    print("               ", date)
	print()
	print("SHIP#      WEIGHT                  VALUE          ")
	print("--------   ---------------------   -------       ")
	
	
	
	weight = 0 
	value = 0 

# select the records to be displayed
	for record in recordList :
		print("%4d      %-10d   %-5d" % record)
		weight = weight + weight1 
		value = value + value1


	print("----------------------------------------------------")
	print("Total WEIGHT: %d" % weight)
	print("Total VALUE:  %d" % value)
	
main()



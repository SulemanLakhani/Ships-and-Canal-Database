# storereport.py
# Created by: Suleman Lakhani
# Date: 09-29-2021
import sys
import getpass
from psycopg2 import connect

# We are going to connect to the database as the user running
# the python program.
dbuser = getpass.getuser()

# Prompt and extract the password used to connect to the db.
dbpass = getpass.getpass()

# Open a connection to the database.
connStr = "host=pascal.rmc.edu dbname=cs236 user=%s password=%s" % (dbuser, dbpass) 
conn = connect( connStr )
  
# Create a database cursor.
dbcursor = conn.cursor()


#print("")
txt = "HOME IMPROVEMENT WAREHOUSE"

print(txt.center(80))
#stores invnum required
invnum = sys.argv[1]


# Query the database for the list of stores.
# fetches store_id, store_city, store_state relating to the invnum
dbcursor.execute("SELECT store_id,store_city, store_state FROM sales.stores NATURAL JOIN sales.transactions WHERE trans_num = %d" % int(invnum))

# Use the tuples.
storeinfo = dbcursor.fetchall()

#print(storeinfo)

print("Invoice #%s".center(80) % invnum)
print()

#prints all tuples
for record in storeinfo :
	print("#%d - %s, %s".center(70) % record)

# fetches trans_date relating to the invnum
dbcursor.execute("SELECT trans_date FROM sales.transactions WHERE trans_num = %d" % int(invnum))
trans_date = dbcursor.fetchall()

date = str("%s" % trans_date[0])

#print("%s" % date)
year = date[0:4]
month = date[5:7]
date = date[8:]
date = month+"/"+date+"/"+year
print("%s".center(70) % date)
print()

print("No.", "PROD-NUM        ", "DESCRIPTION" ," "*25,"CNT  ","PRICE  "," TOTAL")
print("-"*80)

# fetches prod_id, prod_name, num_sold, item_price relating to the invnum
dbcursor.execute("SELECT prod_id, prod_name, num_sold, item_price, \
	num_sold*item_price AS total FROM sales.products NATURAL JOIN \
	sales.trans_items WHERE trans_num = %d" % int(invnum))
productsList = dbcursor.fetchall()

#print(productsList)
i = 1

for record in productsList :
	print("%d.  " % i, end="")
	print("%-15s  %-38s %d %8.2f  %7.2f" % record)
	i = i + 1

print("-"*80)

# gives total for all products sold
dbcursor.execute("SELECT sum(num_sold*item_price) FROM sales.trans_items WHERE trans_num = %d" % int(invnum))
total = dbcursor.fetchall()

print(" "*45, end = "")
print("TOTAL DUE:                   %5.2f" % total[0])

# Close the connection to the database.
conn.close()

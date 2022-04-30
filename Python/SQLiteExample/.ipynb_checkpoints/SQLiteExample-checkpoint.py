import sqlite3

# Makes connection to file in directory or creates one
# if it doesnt already exist
conn = sqlite3.connect('customer.db') 

### Now we want to build a table 

# Creating a cursor
c = conn.cursor() #creates instance of cursor

## creating a table

#create a table using docstrings
#c.execute("""CREATE TABLE customers (
#		first_name text,
#		last_name text,
#		email text
#		)""")

c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@gayboy.com')")


#Commit our command 
conn.commit()

#Close our connection
conn.close()
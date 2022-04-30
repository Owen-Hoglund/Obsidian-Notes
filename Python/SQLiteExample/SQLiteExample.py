import sqlite3

# Makes connection to file in directory or creates one
# if it doesnt already exist
conn = sqlite3.connect('customer.db') 

### Now we want to build a table 

#### Creating a cursor
c = conn.cursor() #creates instance of cursor

##### creating a table

###create a table using docstrings
c.execute("""CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
		)""")

## Inserting one item into the database
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@gayboy.com')")


###inserting multiple items into the table
#many_customer = [
#    ('wes', 'brown', 'wesemail@gay.co.uk'),
#    ('west', 'brownter', 'wesrereemail@gay.co.uk'),
#    ('wt', 'br', 'email@gay.co.uk'),
#]

## the '?'s represent placeholders, and then we pass in the list to fill the placeholders
#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)



##### Query the Database
## This is THE SAME AS SQL!!!
c.execute("SELECT * FROM customers")
##c.fetchone()
##c.fetchmany()

# prints the query
#print(c.fetchall())

#### FORMATTING RESULTS
items = c.fetchall()
for item in items:
    print(item[0] + " " + item[1] + " " + item[2])


#Commit our command 
conn.commit()

#Close our connection
conn.close()


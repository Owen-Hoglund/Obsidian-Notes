Constraints and [[SQL Operators]] add information about how a column can be used and are invoked after specifying the data type for a column. They can be used to tell the database to reject inserted data that does not adhere to a certain restriction. 
For example, the statement below sets _constraints_ on the `celebs` table.

CREATE TABLE celebs (  
   id INTEGER PRIMARY KEY,  
   name TEXT UNIQUE,  
   date_of_birth TEXT NOT NULL,  
   date_of_death TEXT DEFAULT 'Not Applicable'  
);

1. [[Primary and Foreign Keys]] columns can be used to uniquely identify the row. Attempts to insert a row with an identical value to a row already in the table will result in a _constraint violation_ which will not allow you to insert the new row.
2. [[UNIQUE]] columns have a different value for every row. This is similar to `PRIMARY KEY` except a table can have many different `UNIQUE` columns.
3.   [[NOT NULL]] columns must have a value. Attempts to insert a row without a value for a `NOT NULL` column will result in a constraint violation and the new row will not be inserted.
4. [[DEFAULT]] columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.
5. [[WHERE]] - restricts query results to a given specification.

Another example follows
CREATE TABLE awards (  
   id INTEGER PRIMARY KEY,  
   recipient TEXT NOT NULL,  
   award_name TEXT DEFAULT 'Grammy'  
);

creates a table titled awards, where no one row has the same key value, there is a recipient of the award, and the award defaults to Grammy. The only info that could be put in this table is a person who has won a Grammy 


#fix idk do something less messy here



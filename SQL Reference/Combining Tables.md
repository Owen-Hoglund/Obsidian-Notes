Combining Tables With SQL

*`Joining Tables`*
[[JOIN]]
The sequence JOIN allows us to easily combine tables.
```SQL
The sequence JOIN allows us to easily combine tables.
	SELECT *  
	FROM orders  
	JOIN customers  
		ON orders.customer_id = customers.customer_id;
```


#SQLfix
Let’s break down this command:

1.  The first line selects all columns from our combined table. If we only want to select certain columns, we can specify which ones we want.
2.  The second line specifies the first table that we want to look in, `orders`
3.  The third line uses `JOIN` to say that we want to combine information from `orders` with `customers`.
4.  The fourth line tells us how to combine the two tables. We want to match `orders` table’s `customer_id` column with `customers` table’s `customer_id` column.

We use the syntax `table_name.column_name` to specify the columns we want to combine between the two tables

[[LEFT JOIN]]
A left join works similarly to a regular join, but if there are discrepancies on a row between the two columns we are joining on, then preference is given to the data on the left table, so the column joined on will be identical to the table on the left, and any mismatched data on the row that came from the right table will be NULL. 

Oftentimes the tables that you are joining will both be on a special column. These are [[Primary and Foreign Keys|Primary Keys]] and [[Primary and Foreign Keys|Foreign Keys]]. 

[[Cross Join]]
A cross join is when you join two tables not on a column but instead combine all of the rows from another table. 
#example 
```SQL
SELECT * 

FROM newspaper 

CROSS JOIN months;
```

[[Union]]
The UNION operator allows you to stack one dataset on top of another. This is useful for combining tables that have similar/identical columns, but different row data. 
#example 
```SQL
SELECT *  
FROM table1  
UNION  
SELECT *  
FROM table2;
```
SQL requires that when you append data in this way
- Tables must have the same number of columns
- The columns must share the same data types in the same order

[[With]]
Often times, we want to combine two tables, but one of the tables is the result of another calculation.
- The WITH statement allows us to perform a separate query
- `previous_results` is the alias that we will use to reference any columns form the query inside of the WITH clause
With is a very powerful tool as it allows you to create an entire complex query, alias it as something else, and then use it in a following query as though it was part of the database already. 

#example 
```SQL
WITH previous_results AS (  
   SELECT ...  
   ...  
   ...  
   ...  
)  
SELECT *  
FROM previous_results  
JOIN customers  
  ON _____ = _____;
```

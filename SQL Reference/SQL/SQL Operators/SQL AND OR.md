AND is an operator that allows  you to use more than one condition in a [[WHERE]] clause to make the result set more specific and useful.

for example 
	SELECT *   
	FROM movies  
	WHERE year BETWEEN 1990 AND 1999  
		AND genre = 'romance';

Returns only romance movies made between 1990-1999.

The syntax for an OR statement is identical
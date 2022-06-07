In addition to being able to group data using GROUP BY, SQL also allows you to filter which groups to include and which to exclude. 
`HAVING` is very similar to [[WHERE]]. 

#example 
	SELECT year, genre, COUNT(name)  
	FROM movies  
	GROUP BY 1, 2  
	HAVING COUNT(name) > 10;
will return the number (COUNT(name)) of movies of different genres (SELECT year, genre,) were produced each year, but will exclude years and genres with less than 10 movies. 
The GROUP BY 1, 2 specifies that we are grouping by first column (year) and second column (genre) (from line one).


When you want to limit the results of a query based on values of the individual rows, use `WHERE`.
When you want to limit the results of a query based on an aggregate property, use `HAVING`


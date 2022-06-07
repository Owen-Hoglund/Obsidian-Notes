`GROUP BY` is a clause in SQL that is used with aggregate functions. It is used in collaboration with the SELECT statement to arrange identical data into _groups_.  
#example

	SELECT year,  
		AVG(imdb_rating)  
	FROM movies  
	GROUP BY year  
	ORDER BY year;

Will calculate and return the average imdb rating for all movies in a given year in order by year.

Sometimes, we want to GROUP BY a calculation done on a column. 
#example
For instance, we might want to know how many movies have IMDb ratings that round to 1, 2, 3, 4, 5. We could do this using the following syntax:
	SELECT ROUND(imdb_rating),  
	   COUNT(name)  
	FROM movies  
	GROUP BY ROUND(imdb_rating)  
	ORDER BY ROUND(imdb_rating);

However, this query may be time-consuming to write and more prone to error.

SQL lets us use column reference(s) in our `GROUP BY` that will make our lives easier.

-   `1` is the first column selected
-   `2` is the second column selected
-   `3` is the third column selected

and so on.

The following query is equivalent to the one above:
	SELECT ROUND(imdb_rating),  
	   COUNT(name)  
	FROM movies  
	GROUP BY 1  
	ORDER BY 1;
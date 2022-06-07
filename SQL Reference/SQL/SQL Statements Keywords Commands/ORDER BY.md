Order by is a clause that allows you to list the data in the result set in a particular order. 
You can sort results by using ORDER by, either alphabetically or numerically.
#example 
```SQL
SELECT *  
	FROM movies  
	WHERE imdb_rating > 8  
	ORDER BY year DESC;

```
Selects movies where imdb rating is greater than 8 and lists them in descending order by year.

Keywords:

`DESC` is a keyword used in `ORDER BY` to sort the results in _descending order_ (high to low or Z-A).

`ASC` is a keyword used in `ORDER BY` to sort the results in _ascending_ order (low to high or A-Z).

NOTE: The column that you order by doesn't need to be one of the columns we are querying or displaying. 
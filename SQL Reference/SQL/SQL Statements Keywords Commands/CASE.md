A CASE statement allows you to create different outputs (usually in the [[SELECT]] statement). It is SQL's way of handling if-then logic. 
#Example
```SQL
	SELECT name,
		CASE
			 WHEN imdb_rating > 8 THEN 'Fantastic'
			 WHEN imdb_rating > 6 THEN 'Poorly Received'
			 ELSE 'Avoid at All Costs'
		END AS 'Review'
	FROM movies;

```

This lists all the movie names and then sets their rating as 'fantastic', 'poorly received', or 'Avoid at all costs' based on a condition on the imdb rating. The [[AS]] ensures that rather than the column being named 

	" WHEN imdb_rating > 8 THEN 'Fantastic' WHEN imdb_rating > 6 THEN 'Poorly Received' ELSE 'Avoid at All Costs' "

it will be named 'Review'. 

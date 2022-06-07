Filters results based on a given range
For example,
	SELECT *  
	FROM movies  
	WHERE year BETWEEN 1990 AND 1999;

will return every movie made between 1990 and _including_ 1999.

You can do this with letters as well.
	BETWEEN 'A' AND 'J'

will return everything that Begins with an "A" up to and NOT including "J" However it will include something titled simply "J"
Matches zero or more missing letters in a given pattern
For example
	A% matches all items with names that begin with letter 'A'
	%a matches all items with names that end in 'a'

You can also use % both before and after a pattern
	%man% will return all items in the column that contain 'man'
	SELECT *   
	FROM movies  
	WHERE name LIKE '%man%';


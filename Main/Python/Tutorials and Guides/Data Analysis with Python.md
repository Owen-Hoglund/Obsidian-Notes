---
#unfinished
---
These are the notes from watching the video at this [link](https://www.youtube.com/watch?v=r-uOLxNrNk8)
All resources are linked in the youtube description

When to choose R over Python
- High performance
- need R studio

Data Analysis timeline
![[Pasted image 20220415124344.png]]

data analysis v data science
 - data scientists have more coding / math skills
 - data analysts have better communication / business sense


## Dataframes
Dataframes are objects in pandas which are very similar to tables, can be thought of as pandas Series. 
Some common methods 
- df.columns names the columns
- df.index lists the indexes of the dataframe
- df.info gives information about the data types, number of columns, etc
- df.describe will gibe you some statistics about the DF (mean, median, std. dev., etc.,)
- df.types will list the datatypes in each column
##### Indexing, Selection and slicing
- df.loc #def will let you select a row by its index (whatever the index is)
- df.iloc  #def will let you select a row by sequential position (numeric)
- df[] #def will give you a particular column 

##### Conditional Selection (Boolean Array)
- df.loc[df['population' > 70]] 
- Dropping
	- df.drop (lots of options)


All of these operations are _immutable_, they do not actually change the underlying dataframe, they make a copy of the resulting dataframe for viewing or manipulation. 
##### Modifying DataFrame
One can easily add, erase, edit, any column or row or cell of a DF. #finish (add methods)
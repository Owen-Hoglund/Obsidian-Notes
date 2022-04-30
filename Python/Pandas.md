Pandas is an exremely useful and robust data analysis and data science library

### Pandas Series
```Python
import pandas as pd
import numpuy as np
```

A series is an ordered sequence of indexed elements (much like a python list). However, a series has an associated data type. Also you can give a series a name, which will be very useful when you insert a series into a table as a column. 

Series are backed by a numpy array that you can always consult
```Python
type(g7_pop.values)
```

Much like a list in python it has an internal list, however in a series it is much more explicit. Additionally, we can manually and arbitrarily assign the index. For example, rather than have the index be a number, you can assign elements in the series a String (you can also assign these indices on creation).
![[Pasted image 20220415165447.png]]

However, unlike a dictionary in python, a series is ordered. 

#### Conditional Selection
We can select parts of Pandas series with a conditional selection
```Python
g7_pop[g7_pop > 70]
```
The above will return only those countries with a population above 70
![[Pasted image 20220415170335.png]]


#### General notes
- slicing works in pandas but upper limit _IS_ included
- 
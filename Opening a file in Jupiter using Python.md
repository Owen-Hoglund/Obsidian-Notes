To use a data file in jupyter notebooks using python, follow these steps:
1. Find the file that you need to access within the file explorerer (or Everything)
2. Shift + rigth click "Save as path" on the file in question
3. paste the path in quotation marks into the line of python code with an 'r' preceeding it.

## example
```Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

sales = pd.read_csv(
    r'C:\Users\owenh\OneDrive\Desktop\Computer Science\General Data Files\sales_data.csv',
    parse_dates=['Date'])

```

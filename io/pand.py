# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # CSV
#
# Reading, writting and analysing CSV files is achived by using the [pandas](https://pandas.pydata.org) library.
#
# ## Opening a CSV
#
# The reading of CSV files is done by using the [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) method.

# +
import pandas as pd

data = pd.read_csv('./data/nina34.csv', 
                   delim_whitespace=True,  # use spaces as delimiter
                   skipfooter=2,   # skips the last 2 lines
                   na_values=-99.99,  # sets missing values
                   engine='python'  # sets engine to Python (default C does not support skip footer)
                   )
# -

# It returns a [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) object.

# To get the names of the line and columns:

print(data.index) # recovers the labels of the columns
print(data.columns)  # recovers the column indexes

# To display some lines at the beginning or at the end:

# beginning
print(data.head(3))

# end
print(data.tail(3))

# ## Data extraction
#
# To extract data from the DataFrame, you can either 
#
# - extract one column
# - use column/row names
# - use column/row indexes
#
# ### Extracting one column
#
# To extract a whole column:

col = data['JAN']
print(col)

# ### Using names
#
# Extracting data using column and row names is done by using the [loc] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas-dataframe-loc method.

# Extracting one column
dataex = data.loc[:, 'JAN']
print(dataex)

# Extracting one row
dataex = data.loc[1950, :]
print(dataex)

# Combining both
dataex = data.loc[slice(1950, 1953), ['JAN', 'FEB']]
print(dataex)

# ### Using indexes
#
# Extracting data using column and row names is done by using the [iloc] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html#pandas-dataframe-iloc method.

# Extracting one column
dataex = data.iloc[:, 0]
print(dataex)

# Extracting one row
dataex = data.iloc[2, :]
print(dataex)

# Combining both
dataex = data.iloc[slice(2, 6), [0, 1]]
print(dataex)

# ## Extracting data arrays
#
# To extract the data arrays, use the `values` attributes.

# extract_data into arrays
array = data.values  # extracts data, no more metadata (column names, etc)
print(type(array))

# ## Plotting
#
# `pandas` comes with some functions to draw quick plots.

# +
import matplotlib.pyplot as plt

data.loc[:, ['JAN', 'FEB']].plot()
plt.show()
# -

fig = plt.figure()
data.loc[1950, :].plot()
plt.show()

# ## Creating dataframes
#
# To create a data frame is done by using the [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) method.

# +
import numpy as np

# init a date object: 10 elements with a 1h interval
date = pd.date_range('1/1/2012', periods=10, freq='H')

x = np.arange(10)
y = np.arange(10)*0.5
cat = ['A']*2 + ['C'] + ['A'] + 3*['B'] + ['C'] + ['D'] + ['A']

data = pd.DataFrame({'xvalue': x,
                     'yvalue': y,
                     'cat': cat},
                     index=date)
print(data)
# -

# To convert a pandas data time series into a [caterogical](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html) data, use the `.astype("category")` method.

# +
# set into a category (equivalent to R factor)
print('cat')
print(data['cat'])

data['cat_c'] = data['cat'].astype("category")

print('cat_c')
print(data['cat_c'])
print(data['cat_c'].cat.categories.values)  # extract list of categories
# -

# ## Mathematical operations
#
# Mathematical operations can be done by using the available pandas methods. Note that it is done only on numerical types.

# Computes the mean over the entire data frame
datam = data.mean()
print(datam['xvalue'])

# mean over the second dimension (columns)
datam = data.mean(axis=1)
print(datam)

# There is also the possibility to do some treatments depending on the value of a caterogical variable.

datas = data.sort_values(by="cat")
print(datas)

datas =  data.groupby("cat").size()
print(datas)

datas =  data.groupby("cat").size()
print(datas)

datas =  data.groupby("cat").mean()
print(datas)

datas =  data.groupby("cat").std()
print(datas)

# ## Writting a CSV
#
# Writting a CSV file is done by calling the [DataFrame.to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) method.

# +
import numpy as np

# init a date object: 10 elements with a 1h interval
date = pd.date_range('1/1/2012', periods=10, freq='H')

x = np.arange(10)
y = np.arange(10)*0.5
cat = ['A']*2 + ['C'] + ['A'] + 3*['B'] + ['C'] + ['D'] + ['A']

data = pd.DataFrame({'xvalue': x,
                     'yvalue': y,
                     'cat': cat},
                     index=date)

data.to_csv('data/example.csv', sep=';')

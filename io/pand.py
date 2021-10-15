# ---
# jupyter:
#   jupytext:
#     formats: py:light,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
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
                   skipfooter=3,   # skips the last 2 lines
                   na_values=-99.99,  # sets missing values  
                   engine='python'  # sets engine to Python (default C does not support skip footer)
                   )
data
# -

# It returns a [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) object.

# To get the names of the line and columns:

data.index

data.columns

# To display some lines at the beginning or at the end:

data.head(3)

data.tail(3)

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
# To extract a whole column, we can provide a list of column names as follows:

col = data[['JAN', 'FEB']]
col

# ### Using names
#
# Extracting data using column and row names is done by using the [loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas-dataframe-loc) method.

dataex = data.loc[:, ['JAN', 'FEB']]
dataex

dataex = data.loc[[1950, 1960], :]
dataex

dataex = data.loc[1950:1953, ['JAN', 'FEB']]
dataex

# ### Using indexes
#
# Extracting data using column and row names is done by using the [iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html#pandas-dataframe-iloc) method.

dataex = data.iloc[:5, 0]
dataex

dataex = data.iloc[2, :]
dataex

dataex = data.iloc[slice(2, 6), [0, 1]]
dataex

dataex = data.iloc[slice(2, 6), :].loc[:, ['OCT', 'NOV']]
dataex

# ## Extracting data arrays
#
# To extract the data arrays, use the `values` attributes.

array.shape
array

# ## Plotting
#
# `pandas` comes with some functions to draw quick plots.

# +
import matplotlib.pyplot as plt

l = data.loc[:, ['JAN', 'FEB']].plot()
# -

l = data.loc[1970, :].plot()

l = data.T.loc[:, 1995:2000].plot()

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
data
# -

# ## Mathematical operations
#
# Mathematical operations can be done by using the available pandas methods. Note that it is done only on numerical types. By default, the mean over all the rows is performed:

datam = data.loc[:, ['xvalue', 'yvalue']].mean()
datam

# But you can also compute means over columns:

# mean over the second dimension (columns)
datam = data.loc[:, ['xvalue', 'yvalue']].mean(axis=1)
datam

# There is also the possibility to do some treatments depending on the value of a caterogical variable (here, the column called `cat`).

data_sorted = data.sort_values(by="cat")
data_sorted

# You can count the occurrences:

data.groupby("cat").size()

data.groupby("cat").mean()

data.groupby("cat").std()

# ## Writting a CSV
#
# Writting a CSV file is done by calling the [DataFrame.to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) method.

data.to_csv('data/example.csv', sep=';')

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

# ## Dictionaries
#
# ### Definition
#
# A dictionary can be viewed as an *unordered* list of elements (called *values*),  which are *not necessarily of the same type* and are accessible via a unique label, which must be an immutable object (called *keys*).
#
# <img src="figs/tikz_dict.png" alt="Dictionaries" text-align=center width=400>
#
# ### Usage
#
# Dictionaries are used:
#
# - To manipulate the global environment (```globals()``` dictionary)
# - To handle function arguments (```**kwargs``` arguments)
# - Class objects are associated with a dictionary (```__dict__``` attribute)
# - To manipulate some objects (```pandas.DataFrame```, ```xarray.Dataset```)
#
# ### Manipulation 
#
# To have more about dictionaries, visit [python.org](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
#
# #### Creating dictionaries

# Creating dictionary
data = {} # empty dictionary
data = {'dataint':10 , 'datstr':'This is a dictionnary'} # not empty one
print(data)
print(len(data))  # number of elements

# create a dictionary providing a list of keys and a value for all keys
data = dict.fromkeys(['key0', 'key1', 3], 'new val')
print(data)

# #### Accessing elements

# Getting and replacing dict. elements
data = {'dataint':10 , 'datstr':'This is a dictionnary'}
print(data.get('datstr')) # retrieve a value from the key
print(data.get('toto'))  # returns None if toto is not a key
print(data.get('toto', 0))  # returns 0 if toto is not a key
print(data['datstr'])
#data['toto'] # fails!

data['datlist'] = [0, 1, 2] # add a new element to the dict (key=datlist)
data['datstr'] = 'new string'  # overwrites a given value (key=datstr)
print(data)

# +
# datstr is found, value not changed
# returns the value of the new key
added = data.setdefault('datstr', 'final string')
print(added)  # no change in the datstr element

# datstrbis not found, value is set 
added = data.setdefault('datstrbis', 'final string')
print(added)
# -

# check whether dict contains a given key
iskey = ('datstr' in data)
istoto = ('toto' in data)
print(iskey)
print(istoto)

# Getting keys and values
data = {'dataint':10 , 'datstr':'This is a dictionnary'}
keys = list(data.keys())  # list the keys
vals = list(data.values())  # list the values
items = list(data.items())
print(keys)
print(vals)
print(items)
# Note: in Python3, these methods do not return list anymore but iterators
# however, they can be converted to list easily using type conversion

# +
# loop over key,value pairs
for it in data.items():
    print(it)
    
# loop over key,value pairs
for k, v in data.items():
    print('key, val = ', k, v)
    
# same as
for k, v in zip(data.keys(), data.values()):
    print('key, val = ', k, v)
# -

# #### Removing elements

# removing all the content of a dict.
data.clear()  # Removes all the elements
len(data)
print(data)

# Removing an element from key and return the removed values
data = {'dataint':10 , 'datstr':'This is a dictionnary'}
removed = data.pop("datstr")
print(removed)
print(data)

# #### Concatenation

# Concatenate dictionnaries
data = {'dataint':10 , 'datstr':'This is a dictionnary'} # not empty one
data2 = {'dataint':14,' datflt':0.5}
# add the elements of dict data2 into dict data
# note that the dataint of data has been replaced by the dataint of data2
data.update(data2) 
print(data)
print(data2)

data.update(toto='toto var')  # equivalent to data.update({'toto':'toto_var'})

# Putting all the content of the data dict into the globals() dictionary
# which defines all the global variables
# In the variable explorer, you should see all the elements
globals().update(data)
print(dataint)

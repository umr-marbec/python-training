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

# # Dictionaries
#
# ## Definition
#
# A dictionary can be viewed as an *unordered* list of elements (called *values*),  which are *not necessarily of the same type* and are accessible via a unique label, which must be an immutable object (called *keys*).
#
# <img src="figs/tikz_dict.png" alt="Dictionaries" text-align=center width=400>
#
# ## Usage
#
# Dictionaries are used:
#
# - To manipulate the global environment (```globals()``` dictionary)
# - To handle function arguments (```**kwargs``` arguments)
# - Class objects are associated with a dictionary (```__dict__``` attribute)
# - To manipulate some objects (```pandas.DataFrame```, ```xarray.Dataset```)
#
# ## Manipulation 
#
# To have more about dictionaries, visit [python.org](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
#
# ### Creating dictionaries
#
# Creating dictionaries is done by using `{}`. To create an empty one:

data = {} # empty dictionary
data

# To create one with values:

data = {'dataint':10 , 'datstr':'This is a dictionnary'} 
data

# You can also initialize a dictionary by giving the same value to all keys using the `fromkeys` method:

data = dict.fromkeys(['key0', 'key1', 3], 'new val')
data

# ### Accessing elements
#
# Accessing elements is done by using the `get` method:

# Getting and replacing dict. elements
data = {'dataint':10 , 'datstr':'This is a dictionnary'}
data.get('datstr')

# If the key does not exist, nothing is returned:

data.get('toto')

# except if you provide an additional argument, which is the return value if key is not found

data.get('toto', 0)

# To get a dictionary element can also be done using a `dict[key]` syntax. However, this way is not safe since the programs stops if a key is not found:

data['datstr']
# data['toto'] # fails!

# ### Changing/adding values

# To add or overwrite a value in a dict:

data['datlist'] = [0, 1, 2] # add a new element to the dict (key=datlist)
data

data['datstr'] = 'new string'  # overwrites a given value (key=datstr)
data

# In the above, the existing key is overwritten. In order to prevent overwritting, adding elements can be achieved by using the `setdefault` method. If the key already exists, nothing is done and the function returns the old value. If the key does not exist, the dictionary is updated and the associated value is returned.

# If we create a dictionary:

data = {'dataint':10 , 'datstr':'This is a dictionnary'}

# If we try to overwrite an existing key of the dict:

added = data.setdefault('datstr', 'final string')
added, data

# In this case, the dictionary is not updated and the function returns the value that was on the dictionary.
#
# If now we try to add a new key to the dict:

# datstrbis not found, value is set 
added = data.setdefault('datstrbis', 'final string')
added, data

# In this case, the value provided in the argument is returned and the dictionary is updated.
#
# To check if a key is in a dictionary, use the `in` statement:

# check whether dict contains a given key
iskey = 'datstr' in data
istoto = ('toto' in data)
print(iskey)
print(istoto)

# To recover the list of keys:

data.keys()

# To recover the list of values:

data.values()

# To recover the key/values couples as a tuple:

data.items()

# ### Removing elements

data = {'dataint':10 , 'datstr':'This is a dictionnary'}

# To empty a dictionary:

data.clear()  # Removes all the elements
data

# To remove an element based on the value of the key, use the `pop` method (it returns the removed value):

data = {'dataint':10 , 'datstr':'This is a dictionnary'}
removed = data.pop("dataint")
removed, data

# ### Concatenation

# Concatenation is done by using the `update` method. If we have two dictionaries:

data = {'dataint':10 , 'datstr':'This is a dictionnary'} 
data2 = {'dataint':14,' datflt':0.5}

# To send `data2` into `data`:

data.update(data2)
data

# Note that in this case, the `dataint` value of the destination dict has been overwritten by the value of the source dict. You can also use the following syntax:

data.update(keytoto='toto', keylala='lala')  # equivalent to data.update({'toto':'toto_var'})
data

data

# A usage of `update` can be to include all the variables defined in a dictionary accessible into the global working environment, defined in the `globals()` dictionary. For instance, to use `dataint`, which is defined in the `data` dict, we send the content of `data` into `globals()`:

globals().update(data)

dataint

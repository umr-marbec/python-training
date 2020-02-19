import numpy as np

########################### Creating dictionary
data = {} # empty dictionary
data = {'dataint':10 , 'datstr':'This is a dictionnary'} # not empty one
len(data)  # number of elements

# create a dictionary providing a list of keys and a value for all keys
data = dict.fromkeys(['key0', 'key1', 3], 'new val')
print(data)

########################### Getting and replacing dict. elements
data = {'dataint':10 , 'datstr':'This is a dictionnary'}
data['datstr']
data.get('datstr') # retrieve a value from the key
data['toto']
data.get('toto')  # returns None if toto is not a key
data.get('toto', 0)  # returns 0 if toto is not a key


data['datlist'] = [0, 1, 2] # add a new element to the dict (key=datlist)
data['datstr'] = 'new string'  # overwrites a given value (key=datstr)

# datstr is found, value not changed
added = data.setdefault('datstr', 'final string')

# datstrbis not found, value is set 
added = data.setdefault('datstrbis', 'final string')

# check whether dict contains a given key
iskey = ('datstr' in data)
istoto = ('toto' in data)

########################### Getting keys and values
data = {'dataint':10 , 'datstr':'This is a dictionnary'}

print(list(data.keys()))  # list the keys
print(list(data.values()))  # list the valies

# returns a list of (key, value) tuples
print(list(data.items())) 
list(data.items())[0] 
# Note: in Python3, these methods do not return list anymore but iterators
# however, they can be converted to list easily using type conversion

# loop over key,value pairs
for k, v in data.items():
    print('key, val = ', k, v)
    
# same as
for k, v in zip(data.keys(), data.values()):
    print('key, val = ', k, v)
   
############################## remove elements from a dict    
data.clear()  # Removes all the elements
len(data)

# Removing an element from key and return the removed values
data = {'dataint':10 , 'datstr':'This is a dictionnary'}
removed = data.pop("datstr")
print(removed)

##############################  Concatenate dictionnaries
data = {'dataint':10 , 'datstr':'This is a dictionnary'} # not empty one
data2 = {'datint':14,' datflt':0.5}
data.update(data2) # add the elements of dict data2 into dict data
# note that the dataint of data has been replaced by the dataint of data2

data.update(toto='toto var')  # equivalent to data.update({'toto':'toto_var'})

# Putting all the content of the data dict into the globals() dictionary
# which defines all the global variables
# In the variable explorer, you should see all the elements
globals().update(data)
print(dataint)
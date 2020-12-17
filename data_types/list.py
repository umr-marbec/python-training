# ---
# jupyter:
#   jupytext:
#     formats: py:light
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

# ## Lists
#
# ### Definition
#
# A list is an *ordered* sequence of elements, which are *not necessarily of the same type* and are accessible via a unique *index* (integer), which is the element's position within the list.
#
# <figure>
#     <center>
#     <img src="figs/tikz_list.svg" alt="Static typing" text-align=center width=400>
#      <figcaption text-align=center><i>Liste</i></figcaption>
# </figure>
#
#
# <div class='alert alert-info'>
#     <strong>Note. </strong> Python <i>tuple</i> can be viewed as immutable list. []  are replaced by ()
# </div>
#
#
# ### Usage
#    
# Lists are used ([python.org](https://docs.python.org/fr/3/tutorial/datastructures.html)):
#     
# - The script arguments are stored in a list of strings (```sys.argv```)
# - The Python path is stored in a list (```sys.path```)
# - Used in loops (repeat operations over a list of objects)
# - The `dir` function returns methods/attributes as a list of string
# - Might be used as *stacks* (last-in, first-out). Not optimized for first-in, first-out.
# - To handle function arguments (```*args``` arguments)
#
# ### Manipulation
#
# To have more about lists, visit [python.org](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

# #### List creation

# Creates a list
x = []  # empty list
print(x)
x = [1]  # list with 1 in it
print(x)

# #### Adding elements

# Append method: adds an element to an existing list
x.append([1, 2, 3, 4]) # append -> add list in list
x.append('String')
print(x)
print(len(x))
print(x[1])

# Extend method: adds the elements of a list to an existing list
# (list concatenation). Compare x (append) and y (extend)
y = [1]
y.extend([1, 2, 3, 4]) # extend -> add list elements in a list
y.extend('String') # !!! Strings are considered as a list of char!
print(y)
print(len(y))
print(y[1])

# List concatenation can also be done with the "+" symbol
# the sum of list is equivalent to extend
# you can also multiply a list by an integer to repeat the list
####### No numerical operations with lists
x = [0, 1, 2]
y = [3, 4, 5]
z = x + y
print(x + y)
print(2*x)
print(2*y)

# #### Removing elements

# +
# init a list ranging from 15 to 19(!)
x = list(range(15, 20))  

# removes the element at index 2 (i.e. the 3rd element)
# returns the value of the removed element
removed_val = x.pop(2) 
removed_last = x.pop()
print(removed_val, removed_last) 
print(x)

# removes the element with the value 16 2 (i.e. the 3rd element)
# returns the value of the removed element
x.remove(16)
print(x)
# -

# #### List copy

# +
# WARNING WITH THE COPY ASSIGNMENT OF MUTABLE!!!!
# # copy assignment copy references (i.e. memory adresses), not values
# changing the content of a mutable does not change it's memory address
# therefore changing x changes y (and conversely) 
# since they both refer to the same object
x = [1, 2, 3, 4, 5]
y = x
print(id(x), id(y))  # same memory address
x[1] = 30
y[3] = 1000
print(x)
print(y)

x = [1, 2, 3, 4, 5]
y = x.copy()  # make a deep copy of x and store it in an object y
print(id(x), id(y))  # different memory addresses
x[1] = 30 
y[3] = 1000
print(x)
print(y)
# -

# #### Count, reverse, sort

# Counting the number of occurrences of an object
x = [5, 6, 15, 7, 2, 15]
print(x.count(15))

# Reverse the list (in place)
# This is done **in place**
x = [5, 6, 15, 7, 2, 15]
x.reverse()
print(x)

# example of bad syntax
x = [5, 6, 15, 7, 2, 15]
x = x.reverse()
print(x)
# Why does it return None? Because the reverse() method returns
# the reverts the input list, but returns nothing.
# so in here, you attribute to a new object x the output of 
# the reverse method, which is None
help([].reverse)

# Sorting elements (in place)
x = [5, 6, 15, 7, 2, 15]
x.sort()  # sort elements (in place)
print(x)

# #### Elements checking

# Check if element is in the list
is2 = (2 in x)
print(is2)

ind7 = x.index(7)  # finds index of 7 element
print(ind7)
print(x[ind7])
# ind1000 = x.index(1000)  # error because 1000 not in list

# #### List indexing

# +
# List indexing is a delicate part....
# In python, index starts at 0
# But you can access them with negative indexes
x =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 0  1  2  3  4  5  6  7  8  9

print(x)
print(x[0]) # getting first elements
print(x[2:5]) # getting elements from index 2 to index 4(!)

print(x[-1]) # getting last element
print(x[-5:-3]) # getting the elements from 5th to last to 4th(!) to last

print(x[6:]) # getting all the elements starting from index 6
print(x[:3]) # getting all elements from 0 to index 2(!)

# getting elements starting from index 2 
# ending to index -2 with a stride of 2
print(x[2:-2:2]) 
print(x[2:-2:1]) 

print(x[::4]) # getting all the elements with a stride of 2
# -

# note: you can also use the slice function to access list indexes
print(x[3:-2:2]) 
print(x[slice(3, -2, 2)])
help(slice)

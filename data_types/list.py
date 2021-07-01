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

# # Lists
#
# ## Definition
#
# A list is an *ordered* sequence of elements, which are *not necessarily of the same type* and are accessible via a unique *index* (integer), which is the element's position within the list.
#
# <img src="figs/tikz_list.png" alt="Static typing" text-align=center width=400>
#
# <div class='alert alert-info'>
#     <strong>Note. </strong> Python <i>tuple</i> can be viewed as immutable list. []  are replaced by ()
# </div>
#
#
# ## Usage
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
# ## Manipulation
#
# To have more about lists, visit [python.org](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

# ### List creation
#
# The creation of a list is done by using `[]`

# Creates a list
x = []  # empty list
print(x)
x = [1]  # list with 1 in it
print(x)

# ### Adding elements
#
# Two methods are available for adding ellements to a list. First, the `append` method, which adds an element to a list:

x = [1]
x.append([1, 2, 3, 4]) # append -> add list in list
x.append('String')
print(x)
print(len(x))
print(x[1])

# The `x` list now contains 3 elements, one `int`, one `list` and one `string`.
#
# The `extend` method, on the other hand, adds *the elements* of an object to a list. Let's repeat the above operations but using replacing `append` by `extend.

y = [1]
y.extend([1, 2, 3, 4]) # extend -> add list elements in a list
y.extend('String') # !!! Strings are considered as a list of char!
print(y)
print(len(y))
print(y[1])

# The `y` list now contains `int` and `char` elements. The elements of the first list (`1, 2, 3, 4`) have been added. And the characters of the `string` variable as well (in this case, `string` behaves like a list of `char`). `extend` can thus be used for list concatenation.
#
# Another way for concatnating lists is by using `+` or `*` symbol.

x = [0, 1, 2]
y = [3, 4, 5]
print(x + y)
print(2*x)
print(2*y)

# **As you see, `+` and `*` should not be used for mathematical operations on `list`!**

# ### Removing elements
#
# There is two methods to remove elements from a `list`. First, `pop` removes the element whose index is given as argument (if no arguments, the last element is removed). The function returns the value of the removed element.

# +
# init a list ranging from 15 to 19(!)
x = list(range(15, 20))  
print(x)

# removes the element at index 2 (i.e. the 3rd element)
# returns the value of the removed element
removed_val = x.pop(2) 
removed_last = x.pop()
print(removed_val, removed_last) 
print(x)
# -

# The `remove` method removes the element within the list that math the *value* provided as argument. If several elements have the same value, the first occurence is removed. This method does not return anything, contrary to `pop`.

x = [16, 17, 16, 20]
x.remove(16)
x

# ### List copy
#
# The copy of mutable objects, like `list`, must be done carefully. Let's look at the following code:

x = [1, 2, 3, 4, 5]
y = x
print(id(x), id(y))  # same memory address
x[1] = 30
y[3] = 1000
print(x)
print(y)

# In the 2nd line, a copy of x is (presumably) made and assigned to `y`. However, when looking at the memory address of the two objects using `id`, they are the same. Consequently, a modification of one (here `x`) modifies the values of the `other`.
#  
# This is because assigment of mutable copy references (i.e. memory adresses), not values (as for immutable objects). 
#
# The right way to copy a mutable object is by using the `copy` method:

x = [1, 2, 3, 4, 5]
y = x.copy()  # make a deep copy of x and store it in an object y
print(id(x), id(y))  # different memory addresses
x[1] = 30 
y[3] = 1000
print(x)
print(y)

# In this case, the `x` and `y` objects are completely different objects and are therefore independent.

# ### Count, reverse, sort
#
# Some methods allow to investigate and manipulate lists.
#
# To count the number occurrences of an element:

x = [5, 6, 15, 7, 2, 15]
print(x.count(15))

# To reverse a list:

x = [5, 6, 15, 7, 2, 15]
x.reverse()
print(x)

# Note that the `reserve` occurs **in place**. When manipulating list, the common error is to assign the output of the `reverse` function:

# example of bad syntax
x = [5, 6, 15, 7, 2, 15]
x = x.reverse()
print(x)

#  Why does it return `None`? Because the `reverse()` method reverts the input list **in place**, but returns nothing.
#  So in the above, the output of 
#  the reverse method is assigned to `x`, which is `None`

help([].reverse)

# Sorting elements is done in the same way

# Sorting elements (in place)
x = [5, 6, 15, 7, 2, 15]
x.sort()  # sort elements (in place)
print(x)

# ### Check for existence
#
# To check if an element is in a list, you can use the `in` function:

# Check if element is in the list
is2 = (2 in x)
print(is2)

# To get the index of an element (first occurrence), use the `index` method.

ind7 = x.index(7)  # finds index of 7 element
print(ind7)
print(x[ind7])
# ind1000 = x.index(1000)  # error because 1000 not in list

# ### List indexing
#
# The elements can be accessed using their index within the list. Some examples are shown below.

# List indexing is a delicate part....
# In python, index starts at 0
# But you can access them with negative indexes
x =  [0, 1,  2,  3,  4,  5,  6,  7,  8,  9]
x[0] # getting first elements

x[2:5] # getting elements from index 2 to index 4(!)

x[-1] # getting last element

x[-5:-3] # getting the elements from 5th to last to 4th(!) to last

x[6:] # getting all the elements starting from index 6

x[:3] # getting all elements from 0 to index 2(!)

# getting elements starting from index 2 
# ending to index -2 with a stride of 2
x[2:-2:2] 

x[::4] # getting all the elements with a stride of 4

# Note that the `start:end:stride` syntax can be replaced by `slice(start, end, stride)`.

start = 0
end = 6
stride = 2
x[start:end:stride]

x[slice(start,end,stride)]

x[slice(5)]  # equivalent to slice(None, 5, None)

x[slice(3, 7)] # equivalent to slice(3, 7, None)

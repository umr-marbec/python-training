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
# The creation of a list is done by using `[]`. To create an empty list:

x = []  # empty list
x

# To create a list with elements:

x = [1, 'string', map]
x

# ### Adding elements
#
# Two methods are available for adding ellements to a list. First, the `append` method, which adds an element to a list:

x = [1]
x.append([1, 2, 3, 4]) # append -> add list in list
x.append('String')
x

# To get the length of a list:

len(x)

# The `x` list now contains 3 elements, one `int`, one `list` and one `string`.
#
# The `extend` method, on the other hand, adds **the elements** of an object to a list. Let's repeat the above operations but using replacing `append` by `extend.

y = [1]
y.extend([1, 2, 3, 4]) # extend -> add list elements in a list
y.extend('String') # !!! Strings are considered as a list of char!
y

len(y)

# The `y` list now contains `int` and `char` elements. The elements of the first list (`1, 2, 3, 4`) have been added. And the characters of the `string` variable as well (in this case, `string` behaves like a list of `char`). `extend` can thus be used for list concatenation.
#
# Another way for concatnating lists is by using `+` or `*` symbol.

x = [0, 1, 2]
y = [3, 4, 5]
x + y

2 * x

2 * y

# **As you see, `+` and `*` should not be used for mathematical operations on `list`!**

# ### Removing elements
#
# There is two methods to remove elements from a `list`. First, `pop` removes the element whose index is given as argument (if no arguments, the last element is removed). The function returns the value of the removed element.

x = [15, 16, 17, 18, 19]
x

removed_val = x.pop(2) 
removed_val, x

removed_last = x.pop()
removed_last, x

# The `remove` method removes the *first* element within the list that match the *value* provided as argument. This method does not return anything, contrary to `pop`.

x = [16, 17, 16, 20]
x

x.remove(16)
x

# If the value is not found, the `remove` function raises an error.

# ### List copy
#
# The copy of mutable objects, like `list`, must be done carefully. First, let's create one list `x`:

x = [1, 2, 3, 4, 5]

# To copy the `x` list inside a new variable `y`, one natural thing to do would be:

y = x

# However, looking at memory addresses using the `id` command shows that both variable share the same memory address.

id(x), id(y)

# Therefore, if you modify `x`, modifications will also be visible on `y`, and conversely:

x[1] = 30
y[3] = 1000
x, y

# This is because assigment of mutable objects copy the references (i.e. memory adresses), not the values (as for immutable objects). 
#
# The right way to copy a mutable object is by using the `copy` method:

x = [1, 2, 3, 4, 5]
y = x.copy()  # make a deep copy of x and store it in an object y
x[1] = 30 
y[3] = 1000
x, y

# In this case, the `x` and `y` objects are completely different objects and are therefore independent.

# ### Count, reverse, sort
#
# Some methods allow to investigate and manipulate lists.
#
# To count the number occurrences of an element:

x = [5, 6, 15, 7, 2, 15]
x.count(15)

# To reverse a list:

x.reverse()
x

# Note that the `reserve` function works **in place** and returns nothing. Therefore, the following code is wrong:

x = (x.reverse())
x

# Here, the call to `x.reverse()` on the right hand-side effectively reverses the `x` list. But the output of the `reverses()` function (which is `None`) is assigned to a new `x` variable, which overwrites the `x` list.

# Sorting elements is done in the same way (also in place)

x = [5, 6, 15, 7, 2, 15]
x.sort()
x

# ### Check for existence
#
# To check if an element is in a list, you can use the `in` function:

(2 in x)

# To get the index of an element (first occurrence), use the `index` method. For instance, to get the index of element `7`:

ind7 = x.index(7)
ind7

# ### List indexing
#
# The elements can be accessed using their index within the list. **In Python, indexes start at 0.** Some examples are shown below with the following `x` list:

x =  [0, 1,  2,  3,  4,  5,  6,  7,  8,  9]
x

x[0] 

x[2:5] # getting elements from index 2 to index 4(!)

x[-1] # getting last element

x[-5:-3] # getting the elements from 5th to last to 4th(!) to last

x[6:] # getting all the elements starting from index 6

x[:3] # getting all elements from 0 to index 2(!)

# getting elements starting from index 2 
# ending to index -2 with a stride of 2
x[8:2:-1] 

x[::4] # getting all the elements with a stride of 4

# Note that the `start:end:stride` syntax can be replaced by `slice(start, end, stride)`.

start = 0
end = 6
stride = 2
x[start:end:stride]

x[slice(start, end,stride)]

x[slice(5)]  # equivalent to slice(None, 5, None)

x[slice(3, 7)] # equivalent to slice(3, 7, None)

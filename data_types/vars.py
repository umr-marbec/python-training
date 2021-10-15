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

# # Variables
#
# ## Variable assignments
#
# Python is a *dynamical binding* and typing language, contrary to C/C++, Java and Fortran, who are *static binding* (source: [pythonconquerstheuniverse](https://pythonconquerstheuniverse.wordpress.com/2009/10/03/static-vs-dynamic-typing-of-programming-languages/))
#
# **Static typing:**
#
# <img src="figs/static_typing.png" alt="Static typing" text-align=center>
#
# **Dynamic typing:**
#
# <img src="figs/dynamic_typing.png" alt="Dynamic typing">
#
# Therefore, one variable name can be reused for different objects. Variable assignment is done with the ```=``` sign:

x = 1
type(x)

x = 2.3  # float
type(x)

x = 'string'  # string
type(x)

# ## Variables as objects
#
# Python is object oriented. Therefore, each assigned variable is an object. Informations about the objects are accessible via the `type` function:

type(x)  # class of the object

# The list of attributes and methods associated with the object are accessible via the `dir` function.

dir(x)  # list of methods/attributes

# ### Object's attribute
#
# An object's attribute is a data which is associated with the object.
#
# To obtain an object's attribute, the general syntax is `object.attribute`. For instance, multidimensional arrays, which are `numpy.array` objects, have the following attributes:

import numpy as np
x = np.array([0, 1, 2, 3, 4, 5, 6])

x.dtype

x.ndim

x.shape

# ### Object's method
#
# Methods are functions that are associated with an object, which use and eventually modify the object's attributes.
#
# To call an object's method, the general syntax is `object.method(arg1, arg2, ...)`. For instance, to compute the mean of the `numpy.array` defined in the above:

m = x.mean(keepdims=True)
m

s = x.std()
s

# To get some help about a method or a function, use the `help` function:

help(x.mean)

# ### Method vs. function
#
# It should be noted that object's method are not called in the same way as module's functions. For instance, there are two ways to compute the mean of a numpy array. 
#
# It can be done by using the `mean` *method* of the `x` object:

x.mean()  

# Or by using the `mean` *function* of the `numpy` module applied on the `x` object:

np.mean(x)

# <div class='alert alert-info'>
#     <strong>Note: </strong> In this case, the numpy function simply calls the object's method.
#  </div>

# ## Transtyping

# To convert an object to another type:

# convert string to a list
xlist = list(x)
type(xlist)

# ## Testing object's class
#
# A usefull method is the `isinstance` one, which allows to determine whether an object if of a given list of class.

x = [0, 1, 2]
print(isinstance(x, (tuple)))
print(isinstance(x, (list, tuple)))

# ## Object's types: mutable and immutable
#
# There are of **two** main caterogies of objects: (source: [geeksforgeeks](https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/)): 
# - *Mutable objects*: Can change their contents: **list, dict, set and custom objects** (*numpy.arrays* for instance)
# - *Immutable objects*: Can't change their contents: **int, float, bool, string, unicode, tuple**}
#
# For instance, the following statement will raise an error:

x = 'string'
# x[0] = 1

# since string are immutable, although they are close to a list object.

# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Functions
#
# ## Definitions
#
# The creation of functions is achieved with the ```def``` keyword:

# +
import numpy as np

def function(arg1, arg2, arg3=0, arg4=-1):
    # arg1, arg2: compulsory arguments
    # arg3, arg4: additional arguments with default values
    # !!! Additional arguments must be after compulsory ones
    output = arg1 + arg2 + arg3 * (arg1 + arg2) \
            + arg4*(arg1 - arg2)
    
    return output, output**2  # returs a 2 elemt. tuple


# +
x1, x2 = function(1, 2) 
print(x1, x2)

x1, x2 = function(1, 2, arg4=1) 
print(x1, x2)

x1, x2 = function(1, 2, arg3=1)
print(x1, x2)

x1, x2 = function(1, 2, arg3=1, arg4=1)
print(x1, x2)

x = function(1, 2, arg3=1, arg4=1)  # output returned as a tuple
print(x)
x1 = x[0]
x2 = x[1]
print(x1, x2)


# -

# ## Arguments as reference or values
#
# Function arguments that are *immutable* (```int```, 
#     ```float```, etc.) are provided as *values*, i.e. a local copy is made in
#     the function. The argument value is not changed after function return.
#
# Function arguments that are *mutable* (```list```, 
#     ```array```, ```dict```, etc.) are provided as *references*, i.e. memory addresses. They can 
#     therefore be modified from within the function. The argument value may change after function call.
#     

# demonstration of arguments as references/values
def update(x, y):
    print('id before ', id(x))
    x += y
    #x = x + y # this creates a new variable x, leaving x value unchanged
    print('id after.', id(x))


##### applied on immutable (int)
x = 1
update(x, 10)
print(x)

##### applied on immutable (string)
x = 'string arg'
update(x, ' final string')
print(x)

##### applied on mutable (list)
x = [1]
update(x, [2])
print(x)

##### applied on mutable (array)
x = np.array([1, 2, 3])
update(x, 2)   # x has been updated in the function
print(x)

# ## Scope of variables
#
# All the variables declared within the function (arguments included)
# are *local* variables. When leaving the function, the variables are removed.

# +
# demonstration of local variable
x = 10

def function(x):

    x = x + 5
    z = x + 10
    print('func. ', 'x=', x, 'z=', z)

function(x)

print(x)
# print(z)  # causes an error: z undefined
# -

# *Global* variables can be accessed from inside a function:

# +
# by default, global variable
y = 20

def function2():
    print(y)

function2()
# -

# <div class="alert alert-danger">
#   <strong>Warning!</strong> 
#     By default, a variable <strong>that is assigned</strong> within a function is considered as <i>local</i>. It must be declared as <i>global</i> in the function.
# </div>
#

# +
z = 30
x = 10

def function3():

    # to assign new values to the global variables,
    # they need to be declared as 'global'
    global z
    # global x

    z += 10     
    # x += 5 # will crash because x not declared global

function3()
print(z, x)  # z has been updated


# -

# ### Functions: the ```*args``` argument
#
# When the number of arguments is variable, you can use the ```*args``` argument, can contains as many arguments as you want.

# +
def function2(x, y, *args):
    # if args are provided
    # print all the arguments
    # return a tuple
    print('x = ', x)
    print('y = ', y)
    print('args = ', args)
    if len(args) > 0:
        for v in args:
            print('other ', v)

function2(3, 'toto')
function2(3, 'toto', 5.4)
function2(3, 'toto', 5.4, 'z', [0, 3, 4])
# -

# ### The ```**kwargs``` argument
#
# Imagine you want to define a function that normalizes a time-series, i.e. removes the mean and divides by the standard-deviation:
#
# $Y = \frac{X - \overline{X}}{\sigma_X}$
#
# You want that your function should be able to consider all arguments as the ```numpy.mean``` function. You can either copy/paste
# the full list of the ```numpy.mean``` arguments. However:
#
# - This is time-consuming
# - This is error prone  (misspelling, updates)
#
# A better way is to use the ```**kwargs``` argument, which is a dictionnary of arguments.

import numpy as np
def stand(x, **kwargs):
    print('kwargs = ', kwargs)
    m = np.mean(x, **kwargs)
    s = np.std(x)
    print(m.shape)
    return (x - m) / s


x = np.random.normal(loc=0.0, scale=1.0, size=(1000, 100))
out = stand(x)
out = stand(x, axis=0)  # mean computed over the dim 0
out = stand(x, keepdims=True, axis=0)  # keeping the dimensions
# out = stand(x, ddof=1)  # crashes since ddof is no numpy.mean argument

# It is also possible to define several `**kwargs` arguments by using dictionaries. 
# For instance, if the user also wants that the `stand` function may also use all the arguments of the `numpy.std` function:

# +
def stand(x, argsmean={}, argsstd={}):
    m = np.mean(x, **argsmean)
    s = np.std(x, **argsstd)
    print('mean', m.shape)
    print('std' , s.shape)
    print('---')
    return (x - m) / s

# extra arguments for the plot function
args_mean = {'keepdims':True, 'axis':0}
# extra arguments for the savefig function
args_std = {'keepdims':True, 'axis':0, 'ddof':1}

out = stand(x)
out = stand(x, argsmean=args_mean)  # mean computed over 1st dimensions
out = stand(x, argsstd=args_std)  # std computed over 1st dimension, removes one dof
out = stand(x, argsmean=args_mean, argsstd=args_std)
# out = stand(x, argsmean=args_std, argsstd=args_mean) # crashes since ddof is no argument for std
# -

# ## Functions: defining input and output types
#
# To manage input and output types, see https://docs.python.org/3/library/typing.html. This is done by using `:` after the argument name. 
#
# **The function will work without any problems, but the linters (VSCode or other) will show that there is a typing issue.**

# +
import numpy as np
def function(x : np.ndarray) -> list:
    output = 2 * x
    return output

function(5)
function(np.array(5))


# -

# ## Lambda functions
#
# Lambda function, also called anonymous functions, are not defined by using 
# the ```def``` statement but the ```lambda``` one.
#
# More on lambda functions can be found in [w3schools](https://www.w3schools.com/python/python_lambda.asp)

y = lambda x: x**2 
print(y(2))
print(y(3))

z = lambda x, y : x * y
print(z(3, 5))
print(z(5, 7))


# An good example of use of lambda functions is provided in [stackoverflow](https://stackoverflow.com/questions/890128/why-are-python-lambdas-useful). In order to generate easily create a multiplicator function, one can use a combination of standard and lambda function.

# Takes as argument the value by which variables should be multiplied
def mulgenerator(n):
    return  (lambda x : x * n)


# Here, the  `mulgenerator`  function returns a lambda  function, i.e. an object that is callable.

# +
# doubler 
doubler = mulgenerator(2)
print(type(doubler))
print(doubler(10))

# quadrupler
quadrupler = mulgenerator(4)
print(quadrupler(10)) 

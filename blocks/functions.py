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

# # Functions
#
# ## Definitions
#
# The creation of functions is achieved with the ```def``` keyword.
#
# Compulsory arguments are put at the beginning of the function definition. The order matters.
#
# Optional arguments are put at the end of the function definition, along with their default values (defined by an `=` statement). The order does not matter here.
#
# Output values are specified using the `return` function. Several variables can be returned (will be returned as `tuple`).

# +
import numpy as np

def myfunc(arg1, arg2, arg3=0, arg4=-1):
    print('args = ', arg1, arg2, arg3, arg4)
    output = arg1 + arg2 + arg3 * (arg1 + arg2) \
            + arg4*(arg1 - arg2)
    
    return output, np.power(output, 2)  # returs a 2 elemt. tuple


# -

x1, x2 = myfunc(1, 2) 
x1, x2

x1, x2 = myfunc(1, 2, arg4=1) 
x1, x2

x1, x2 = myfunc(1, 2, arg3=1)
x1, x2

x1, x2 = myfunc(1, 2, arg3=1, arg4=1)
x1, x2

x = myfunc(1, 2, arg3=1, arg4=1)  # output returned as a tuple
x


# ## Arguments as reference or values
#
# Function arguments that are *immutable* (```int```, 
#     ```float```, etc.) are provided as *values*, i.e. a local copy is made in
#     the function. The argument value is not changed after function return.
#
# Function arguments that are *mutable* (```list```, 
#     ```array```, ```dict```, etc.) are provided as *references*, i.e. memory addresses. They can 
#     therefore be modified from within the function. The argument value may change after function call.

# For instance, let's define a function that adds a `y` variable to a `x` variable:

def update(x, y):
    x += y


# Let's apply the method on an immutable type, for instance an `int`:

x = 1
update(x, 10)
print(x)

# In this case, the `x` value is the same as before. This is because for imutable types, the `+=` statement ultimately creates a new instance (in this case, it is equivalent to `x = x + y`). Same thing holds for a `string` argument:

x = 'string arg'
update(x, ' final string')
print(x)

# Now, let's try to use the function on a mutable type. If we convert the above strings into lists:

x = list('string arg')
update(x, list(' final string'))
print(x)

# In this example, after the function call, the value of `x` is changed. Same holds for arrays:

x = np.array([1, 2, 3])
update(x, 2)   # x has been updated in the function
print(x)

# **Therefore, when modifying a variable argument inside a function, be carefull.**

# ## Scope of variables
#
# All the variables assigned within the function (arguments included)
# are *local* variables. When leaving the function, the variables are removed.

# +
x = np.arange(5)
print('x before ', x)

def function(x):
    print('x begin func ', x)

    x += 5
    
    z = x + 10
    print('x end func', x, 'z', z)

function(np.arange(5, 10))

print('x after ', x)
#print(z)  # causes an error: z undefined
# -

# In the above example, the first print in the function shows the values of the array provided in the function call (`np.arange(5, 10)`). The `x` variable defined above cannot be accessed anymore because overwritten by the local one. When the function ends, the local `x` is destroyed, and the firstly defined `x` is shown by the last print. `z` is only accessible from inside the function.

# *Global* variables, defined outside of a function, can be accessed from inside a function if they are note overwritten by local ones. **But they are accessed in read-only mode only!**

# +
# by default, global variable
y = 20

def function2():
    print(y)

function2()
# -

# To overwrite the value of a global variable from inside a function, it must be declared as `global`:
#

# +
z = 30
x = 10

def function3():

    global z
    
    z = z + 10     
    #x = x + 5 # will crash because x not declared global

function3()
z, x


# -

# In the above example, we can assign a value to the `z` variable although it is not a function argument, because it is declared `global`. However, the same thing on `x` will fail.

# ### Functions: the ```*args``` argument
#
# When the number of arguments is variable, you can use the ```*args``` argument in the function definition. It allows to define any number of additional arguments, which will be provided as a list.

def function2(x, y, *args):
    print('x = ', x)
    print('y = ', y)
    print('args = ', args)


function2(3, 'toto')

# Here, no additional argument is provided. Therefore, an empty list is stored in the `args` variable. 

function2(3, 'toto', 5.4)

# Here, one additional argument has been provided. `args` is therefore a list containing one `float` element.

function2(3, 'toto', 5.4, 'z', [0, 3, 4])

# Here, 3 additional arguments are provided. Note that the additional arguments can be of any type, as done in the above.

# ### The ```**kwargs``` argument
#
# The `**kwargs` arguments allow to provide additional keyword arguments, provided as a `dict`, contrary to `args`, which returns arguments as a `list`. In this case, the arguments are provided using the `key = value` syntax.
#
# Imagine you want to define a function that normalizes a time-series, i.e. removes the mean and divides by the standard-deviation:
#
# $Y = \frac{X - \overline{X}}{\sigma_X}$
#
# Your function should be able to include all the possible arguments of the ```numpy.mean``` function. You can either copy/paste
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


# In your function, you allow the possibility to include to your function call a list of keyword arguments. These keyword arguments are used in the `np.mean` function. Therefore, all the keyword arguments of the `numpy.mean` function can be used in your `stand` function. Let's give it a try by creating a dummy variable.

x = np.random.normal(loc=0.0, scale=1.0, size=(1000, 100))
x.shape

# Now, we call the `stand` function on this array:

out = stand(x)
out.shape

# Here, no keyword arguments has been provided, so the call to the `np.mean` function computes the mean over the entire table, hence returning a numerics. `kwargs` is an empty `dict` object.
#
# Now, if we want to specify the axis along which the mean must be computed:

out = stand(x, axis=0)

# In this case, `kwargs` is a dictionary containing one `key/value` couple. In this case, the `mean` returns an array of size $100$. We can use other arguments that are available on the `np.mean` function:

out = stand(x, keepdims=True, axis=0)  # keeping the dimensions


# However, if you provide a keyword argument that does not exist in the `numpy.mean`, the code will crash.

# +
#out = stand(x, ddof=1)  # crashes since ddof is no numpy.mean argument
# -

# It would be even better if all the arguments of the `np.std` function could be used as well. It is possible by using dictionaries as arguments (instead of `**kwargs`), as done as follows:

def stand(x, argsmean={}, argsstd={}):
    m = np.mean(x, **argsmean)
    s = np.std(x, **argsstd)
    print('mean', m.shape)
    print('std' , s.shape)
    return (x - m) / s


# In this case, we add two optional dictionary arguments (empty by default), one dictionary containing the arguments that will be used in `np.mean` function (`argsmean`), and one dictionary containing the arguments that will be used in `np.std` function (`argsstd`).

# Now we can create the dictionary arguments as follows:

# +
# extra arguments for the plot function
args_mean = {'keepdims':True, 'axis':0}

# extra arguments for the savefig function
args_std = {'keepdims':True, 'axis':0, 'ddof':1}
# -

# Now we can see what happens when we call the new `stand` function, with or without the dict arguments:

out = stand(x)

out = stand(x, argsmean=args_mean)  # mean computed over 1st dimensions

out = stand(x, argsstd=args_std)  # std computed over 1st dimension, removes one dof

out = stand(x, argsmean=args_mean, argsstd=args_std)

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


# An good example of use of lambda functions is provided in [stackoverflow](https://stackoverflow.com/questions/890128/why-are-python-lambdas-useful). In order to generate a multiplicator function, one can use a combination of standard and lambda function.

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
# -

# ## Loading your libraries
#
# If you want to load your own function, stored in a `mylib.py` file, you first need to add your library directory to the `PYTHONPATH`. At the beginning of your script, add:
#
# ```
# import sys
# sys.path.append('/add/other/directory/')
# import mylib
# ```
#
# **When the PYTHONPATH is modified this way, it is only valid for the current Python script.**
#
# In order to change the Python default paths, you need to create a `PYTHONPATH` environment variable. With Mac Os X/Linux, edit your `.bashrc` or `.cshrc` file and add:
#
# ```
# # bashrc
# export PYTHONPATH=${PYTHONPATH}:/add/other/directory
# # cshrc
# setenv PYTHONPATH /add/other/directory:${PYTHONPATH}
# ```
#
# In Windows, see for instance [oracle.com](https://docs.oracle.com/en/database/oracle/r-enterprise/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)
#
# Then, in your Python script, you can use your function as follows:
#
# ```
# mylib.function1
# ```

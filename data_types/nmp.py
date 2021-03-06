# ---
# jupyter:
#   jupytext:
#     formats: py:light,ipynb
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

# # Arrays
#
# ## Usage
#
# The Python ```list``` and ```dict``` objects are not suitable to manage multi-dimensional arrays. 
#
# Instead, the [Numpy](https://numpy.org/) (Numerical Python) library should be used. It allows to:
#
# - Create multi-dimensional arrays
# - Access array attributes (shape, number of dimensions, data types)
# - Manipulate arrays (changing shape, tiling)
# - Manipulate missing values
# - Perform optimized numerical operations (pointwise or matrix) via broadcasting (no loops)

# ## Array manipulation

# ### Array initialisation

# +
import numpy as np 

x = np.arange(0, 10, 1) # equivalent to Matlab 0:1:9
print(x)
# -

x = np.linspace(10, 20, 41) # 10 to 20 with 41 values
print(x)

x = np.array([1, 2, 3, 4, 5]) # initialisation from list 
print(x)

x = np.ones((2, 3, 8), dtype=int) # init with 1 integers
print(x)

x = np.zeros((2, 3, 8)) # init with 0 floats 
print(x)

x = np.empty((2, 3, 8), dtype=float) # init with random floats 
print(x)

x = np.full((2, 3, 8), 10.10)  # fill array with 10.1
print(x)

# ### Changing data type

x = x.astype(int)  # conversion from floats to int
print(x)

# ### Getting attributes

print(type(x)) 
print(x.ndim)  # number of dims
print(x.shape) # tuples containing the dimensions
print(x.dtype) # type of the content

# ### Indexing

# +
x = np.ones((2, 3, 8), dtype=float)

# indexing: same indexing as for lists for any array dimensions
print(x[:, :, 0].shape)
print(x[:, -1, ::2].shape) # (2,3) (2,4) array subspans
# -

# Using `...`, you can also access an array without fully knowing it's shape:

x[..., 0].shape

x[-1, ...].shape

# `list` `numpy.array` can be used to index `numpy.array`, but prefer using `slice` instead. Indeed, using the former may be error prone. Indeed, for extracting a subspan of an array, you might want to use:

x = np.reshape(np.arange(20 * 10), (20, 10))
i = [0, 1, 2, 3]
j = [5, 6, 7, 8]
x[i, j]

# This is equivalent to:

for tmpi, tmpj in zip(i, j):
    print(x[tmpi, tmpj])

# Beside, this will fail if `i` and `j` have different sizes. The proper syntaxt would be:

i = slice(0, 4)
j = slice(5, 9)
x[i, j]

# The values obtained in the in the first try are the elements in the diagonal of the subspan.

# ### Copy

# +
# copies: arrays are mutable, take care with copy assignments
x = np.arange(10)
y = x
y[0] = -1
x[-1] = 1000
print(x)
print(y)
print(id(x), id(y))

x = np.arange(10)
y = x.copy()  # deep copy of x into y 
y[0] = -1
x[-1] = 1000
print(x)
print(y)
print(id(x), id(y))
# -

# ### Reshaping

# Reshaping
x = np.zeros((6, 4))
for i in range(6):
    x[i, :] = np.arange(4) + i*4
print(x)

x1dc = np.ravel(x)   # converts ND to 1D following C order
print(x1dc)

# equivalent to:
N = np.prod(x.shape)
output = np.zeros(N)
cpt = 0
for i in range(x.shape[0]):  # starts with first dimensionss
    for j in range(x.shape[1]):
        output[cpt] = x[i, j]
        cpt += 1
print(np.all(output == x1dc))

# Order=Fortran: the order of the loops is reversed (outer dim to inner dim)
x1df = np.ravel(x, order="F")
print(x1df)

# equivalent to:
N = np.prod(x.shape)
output = np.zeros(N)
cpt = 0
for j in range(4):  # starts with outer dimension!
    for i in range(6):
        output[cpt] = x[i, j]
        cpt += 1
print(np.all(output == x1df))

## Changing the shape of the array in C order
xresc = np.reshape(x, (2, 3, 4)) 
print(x.shape)
print(xresc.shape)

# equivalent to
xresc_t = np.zeros((2, 3, 4))
temp = np.ravel(x)
cpt = 0        
for i in range(2):
    for j in range(3):
        for k in range(4):
            xresc_t[i, j, k] = temp[cpt]
            cpt += 1
print(np.all(xresc_t == xresc))

xresf = np.reshape(x, (2, 3, 4), order="F") # reshape following Fortran order
print(xresf.shape)

# identical to
cpt = 0
xresf_t = np.zeros((2, 3, 4))
temp = np.ravel(x, order='F')
for k in range(4):
    for j in range(3):   # loop orders are reversed in Fortran order
        for i in range(2):
            xresf_t[i, j, k] = temp[cpt]
            cpt += 1
print(np.all(xresf_t == xresf))

# To reshape the array from ND to 2D, by keeping one dimension unchanged:

import numpy as np
x = np.reshape(np.arange(2 * 3 * 4), (2, 3, 4))
xshape = x.shape
xtest = np.reshape(x, (2, -1))  # keeps first dim but transforms (3, 4) in 12
print(xtest.shape)
xtest2 = np.reshape(x, (-1, 4))  # keeps last dim but transforms (2, 3) in 6
print(xtest2.shape)

# ### Repeating along a given dimensions

# repeating an array along given dimensions
# Carefull: the virtual dimensions (1) should be placed in the last positions!
x = np.arange(10)
xtile = np.tile(x, (2, 1)) # (2 ,10) equivalent to repmat
xtile2 = np.tile(x, (1, 2)) # (1, 20)
print(xtile.shape, xtile)
print(xtile2.shape, xtile2)

# Note the difference. When using `tile`, the tiling dimensions must be put first. It sometimes requires the use of `transpose` to have the right size.

# ### Changing dimension order

# changing dimension orders
x = np.ones((5, 10, 15))
xt = np.transpose(x) # identical to xt = xt.T
xt2 = np.transpose(x, (2, 0, 1)) # (15, 5, 10)
print(x.shape)
print(xt.shape)
print(xt2.shape)

# ### Testing conditions

############################################### testing on array
x = np.reshape(np.arange(24), (2, 3, 4))
print(x)
condition = (xresc <= 12) & (xresc >= 3)  # array of boolean (True if condition is met)
print(condition)

# display values where condition is met
print(xresc[condition])

ind = np.nonzero(condition)   # returns a tuple of the i, j, k indexes pairs that match conditions
print(ind)
print(ind[0])  # extracts the i indexes
print(xresc[ind])   # extracts the values that match the condition (1D array)

# extract unique values
x = np.array([0, 0, 0, 1, 2, 2, 3, 3, 3, 3])
print(np.unique(x))

# ### Concatenation

# +
# concatenation
x = np.zeros((2, 3, 5))
y = np.ones((2, 7, 5))

# concatenates x, y along their second dim. dim[0] and dim[2] must have the same values
z = np.concatenate((x, y), axis=1)  
print(z.shape)
# -

# ## Operations using arrays 
#
# ### Multi-arrays in computer memory
#
# Computer memory is inherently linear, i.e. multi-dimensional arrays are stored in memory as one-dimensional arrays. This can be done in two ways:
#
# - Row-major order: C/C++, *Python*
# - Column-major order: Fortran, Matlab, R, Julia
#
# **Row-major order:**
#
# <img src="figs/corder.svg" alt="Dictionaries" text-align=center width=200>
#  
# **Column-major order:** 
#
# <img src="figs/forder.svg" alt="Dictionaries" text-align=center width=200>
#
# ### Loops
#
# This has implications when writting loops. Indeed, imbricated loops should be consistent with the memory ordering:
#
# **Row-order (Python)**
#
# ```
# import numpy as np
# x = np.empty((5, 10))
# for i in range(5):  # inner loop: 1st dim
#     for j in range(10):  # outer loop: last dim
#         print(x[i, j])
# ```
#
# **Column-order (Julia)**
#
# ```
# x = zeros(Int8, 5, 10)
# for j = 1:10   # inner loop: last dim
#     for i = 1:5  # outer loop: 1st dim
#         println(x[i, j])
#     end
# end
# ```
#
# Sources: [Wikipedia](https://en.wikipedia.org/wiki/Row-_and_column-major_order),  [thegreenplace](https://eli.thegreenplace.net/2015/memory-layout-of-multi-dimensional-arrays/)
#
# Let's see with a quick example, using the following array

# +
import numpy as np

shape = (30, 40, 50, 800)
x = np.random.rand(shape[0], shape[1], shape[2], shape[3]).astype(float)
x.shape
# -

# %%time
total = 0
N = 0
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            for l in range(shape[3]):
                total += x[i, j, k, l]
                N += 1
total /= N
total

# %%time
total = 0
N = 0
for l in range(shape[3]):
    for k in range(shape[2]):
        for j in range(shape[1]):
            for i in range(shape[0]):
                total += x[i, j, k, l]
                N += 1
total /= N
total

# The last loop is slower than the first one because the loop order is not consistent with the C-order used in Python.
#
# Note: The `np.ndenumerate` method alows to loop in an array without risk.

cpt = 0
for k, v in np.ndenumerate(x):
    if(cpt == 15):
        break
    print(k, x[k])
    cpt += 1

# The `np.nditer` allows to so similar things:

cpt = 0
for v in np.nditer(x):
    if(cpt == 15):
        break
    print(v)
    cpt += 1

# **Note that the use of `nditer` is read-only. To modify the input array:**

cpt = 0
with np.nditer(x, op_flags=['readwrite']) as it:
    for v in it:
        if(cpt == 15):
            break
        v[...] = 2 * v
        cpt += 1

cpt = 0
for v in np.nditer(x):
    if(cpt == 15):
        break
    print(v)
    cpt += 1

# For more details about iteration, visit [arrays.nditer](https://numpy.org/doc/stable/reference/arrays.nditer.html).
#
# Since the loops are not efficient in Python, it is better not to use them! Therefore, use vectorized functions.

# %%time
tot = x.mean()
tot

# ### Arhtimetical operations
#
# In Python, standard operations are performed pointwise (contrary to Matlab for instance). To do matrix operations, you need to call specific methods (`numpy.matmul` for instance).

# maths: pointwise operations
x = np.array([1, 2, 3, 4, 5]).astype(float)
y = np.array([6, 7, 8, 9, 10]).astype(float)
print(x * y)
print(y / x)
print(y // x)
print(y % x)
print(x**y)

x[2] = 0.
x[3] = -1.
x

z = y / x
z

z = np.divide(y, x, where=(x!=0), out=np.full(x.shape, np.nan, dtype=x.dtype))  # no more warning message
z

w = np.log10(x)
w

w = np.log10(x, where=(x > 0), out=np.full(x.shape, np.nan, dtype=x.dtype))
w

# ### Mathematical operations (mean, etc.)

# +
x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [7, 1, 3, 5, 6, 7, 8, 10, 4, 6],
             [5, 1, 0, 3, 5, 8, 12, 5, 8, 1]])

out = np.mean(x) # compute mean over first dimension
print(out)
# -

out = np.std(x, axis=1) # compute standard deviation over second dimension
print(out)

out = np.sum(x, axis=0) # compute sum over first dimension
print(out)

out = np.cumsum(x, axis=0) # compute sum over first dimension
print(out)

out = np.prod(x, axis=0) # computes the prod along the first dimension
print(out)

x = np.reshape(np.arange(24), (2, 3, 4))
xmean = np.mean(x, axis=(0, 1))  # computes mean over the 1st and 2nd dims
print(xmean.shape)

# ## Broadcasting
#
# In order to avoid loops, it is strongly advised to use broadcasting rules (cf. [docs.scipy](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html))

x = np.reshape(np.arange(24), (2, 3, 4))

xmean = np.mean(x, axis=0)  # mean over the first dimension
print(xmean.shape, x.shape)
anom = x - xmean    

# The code above works because the last (i.e. trailing) two dimensions are the same.

xmean = np.mean(x, axis=-1)
print(xmean.shape, x.shape)
# anom = x - xmean  # 

# In the above, the computation of anomalies because the *first* (i.e leading) dimensions are the same, which does not allow broadcasting. This can be fixed by using the `keepdims` argument. It will keep a virtual dimension on the mean output.

xmean = np.mean(x, axis=-1, keepdims=True)
print(xmean.shape, x.shape)
anom = x - xmean    
# work because virtual dimensions (1) can be broadcasted

# If you are lazy to remember the broadcasting rules, you can use the `numpy.newaxis` method to add virtual dimensions.

y = np.zeros((5, 2, 7, 3, 10, 4))
print(y.shape)
print(x.shape)
xnd = x[np.newaxis, :, np.newaxis, :, np.newaxis, :]
print(xnd.shape)
z = y * xnd
print(z.shape)

# In the above, the `x` array dimensions are consistent with the 2nd, 4th and 6th dimension of `y`. Therefore, a virtual dimension has been added at the 1st, 3rd and 5th location.

# ## Managing filled values
#
# Filled values are generally defined as `numpy.nan` values.

# numpy nans
x = np.arange(1, 10).astype(float)
print(x)
x[0] = np.nan
print(x)

# Checking whether values are `NaN` is achieved by using the `np.isnan` method

np.nonzero(np.isnan(x))

# An equivalent to the `np.isnan` method is to use the mathematical definition of `NaNs`.

np.nonzero(x != x) # Mathematical definition of NaN

# **Warning: `NaNs` can only be used with Float arrays (not integer arrays)**

# +
x = np.arange(1, 10).astype(float)
x[0] = np.nan
print(x)

x = np.arange(1, 10).astype(int)
#x[0] = np.nan
# -

# ### Operations on filled values
#
# To perform operations on data containing `NaNs` requires the use of special functions:

# Use special functions to handle NaNs
print(np.nanmean(x))
print(np.nansum(x))
print(np.nanstd(x))

# Since this can be a bit annoying, `numpy.array` objects can be converted into `masked_array` objects
#
# ### Masked array

# numpy.ma (masked arrays)
x = np.arange(1, 10).astype(int)
print(type(x))

# To convert an array into a masked array, the following methods can be used:

x = np.ma.masked_where(x==0, x) # mask data where 0
x = np.ma.masked_equal(x, 5)    # mask x when equal to 5
x = np.ma.masked_greater(x, 7)  # mask x when greater than 7
x = np.ma.masked_less(x, 3)     # mask x when less than 3
x[2] = np.ma.masked  # mask second elements
print(type(x))
print(x)

# This new object has additional attributes and method. Especially for assessing where the filled values are located.

print(x.mask)    # new attribute as appeared
print(np.ma.getmask(x))  # equivalent to x.mask but works also on unmasked arrays
print(np.mean(x))  # no more need to do a NaN mean
print(np.sum(x))
print(np.std(x))

# It is strongly advised to use the `np.ma.getmask` method rather than using the `mask` attribute. Indeed, the latter will return a `bool` instead of an array of `bool` if no data is missing. 

# warning for masked_arrays
x = np.arange(10, 15).astype(float)
x = np.ma.masked_where(np.isnan(x), x)
print(x)
print(x.mask)


# Therefore, extracting all non missing values from an array is not safe using `mask`:

iok = np.nonzero(x.mask == False)  #  for unmasked values
print(x[iok])  # returns only first value

# However, it works perfectly using the method:

# to get a mask array of the same size as x, use the getmaskarray method
print(np.ma.getmaskarray(x))
iok = np.nonzero(np.ma.getmaskarray(x) == False)  #  for unmasked values
print(x[iok])  # returns all the values

# # Scientific Python
#
# Although the Numpy library allows to do some operations, it is rather limited.
# Other mathematical functions are provided by the [Scipy](https://www.scipy.org/) library. 
#
# <div class="alert alert-success">
# <i>In an ideal world, NumPy would contain nothing but the array data type and the most basic operations: indexing, sorting, reshaping, basic elementwise functions, etc. All numerical code would reside in SciPy. [...] If you are doing scientific computing with Python, you should probably install both NumPy and SciPy. Most new features belong in SciPy rather than NumPy.</i> Source: <a href=\"https://www.scipy.org/scipylib/faq.html#what-is-the-difference-between-numpy-and-scipy" target=\"_blank\">Scipy FAQ</a>
# </div>
#
# ## Submodules
#
# Scipy comes with numerous submodules, which are listed below (source: [scipy.org](https://www.scipy.org/)}
#
#
# | Description                               | Module
# | :----------------------------------------:|:----------------------------:
# | Special functions (mathematical physics)  | [scipy.special](https://docs.scipy.org/doc/scipy/reference/tutorial/special.html)
# | Integration                               | [scipy.integrate](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html)
# | Optimization                              |[scipy.optimize](https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html)
# | Interpolation                             |[scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html)
# | Fourier Transforms                        |[scipy.fft](https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html)
# | Signal Processing                         |[scipy.signal](https://docs.scipy.org/doc/scipy/reference/tutorial/signal.html)
# | Linear Algebra                            |[scipy.linalg](https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html)
# | Spatial data structures and algorithms    | [scipy.spatial](https://docs.scipy.org/doc/scipy/reference/tutorial/spatial.html)
# | Statistics | [scipy.stats](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
# | Multidimensional image processing         | [scipy.ndimage](https://docs.scipy.org/doc/scipy/reference/tutorial/ndimage.html)
# | File IO: Matlab, NetCDF, IDL              |  [scipy.io](https://docs.scipy.org/doc/scipy/reference/tutorial/io.html)
#
# <div class="alert alert-warning">
#     <strong>Since you all are fluent in using Numpy, I leave it to you the exploration of Scipy... </strong>
# </div>

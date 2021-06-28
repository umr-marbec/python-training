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

# # Arrays
#
# ## Usage
#
# The Python ```list``` and ```dict``` objects are not suitable to manage multi-dimensional arrays. 
#
# Instead, the [Numpy](https://numpy.org/) (Numerical Python) library should be used. It allows to:
#
# - Create multi-dimensional arrays}
# - Access array attributes (shape, number of dimensions, data types)
# - Manipulate arrays (changing shape, tiling)
# - Manipulate missing values
# - Perform optimized numerical operations (pointwise or matrix) via broadcasting (no loops)
#
# ## Multi-arrays in computer memory
#
# Computer memory is inherently linear, i.e. multi-dimensional arrays are stored in memory as one-dimensional arrays. This can be done in two ways:
#
# - Row-major order: C/C++, Python
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
#
# ## Consequences for loops
#
# Imbricated loops should be consistent with the memory ordering:
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
# ## Array manipulation
#

import numpy as np

# ### Array initialisation

x = np.arange(0, 10, 1) # equivalent to Matlab 0:1:9
print(x)

x = np.linspace(10, 20, 41) # 10 to 20 with 41 values
print(x)

x = np.array([1, 2, 3, 4, 5]) # initialisation from list 
print(x)

x = np.ones((2, 3, 8), dtype=np.int) # init with 1 integers
print(x)

x = np.zeros((2, 3, 8)) # init with 0 floats 
print(x)

x = np.empty((2, 3, 8), dtype=np.float) # init with random floats 
print(x)

x = np.full((2, 3, 8), 10.10)  # fill array with 10.10
print(x)

# ### Changing data type

x = x.astype(np.int)  # conversion from floats to int
print(x)

# ### Getting attributes

print(type(x)) 
print(x.ndim)  # number of dims
print(x.shape) # tuples containing the dimensions
print(x.dtype) # type of the content

# ### Indexing

# +
x = np.ones((2, 3, 8), dtype=np.float)

# indexing: same indexing as for lists for any array dimensions
print(x[:, :, 0].shape)
print(x[:, -1, ::2].shape) # (2,3) (2,4) array subspans
# -

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
xtest = np.reshape(x, (2, -1))  # keeps 2 but transforms (3, 4) in 12
print(xtest.shape)

# ### Copy along given dimensions

# repeating an array along given dimensions
# Carefull: the virtual dimensions (1) should be placed in the last positions!
x = np.arange(10)
xtile = np.tile(x, (2, 1)) # (2 ,10) equivalent to repmat
xtile2 = np.tile(x, (1, 2)) # (1, 20)
print(xtile.shape, xtile)
print(xtile2.shape, xtile2)

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

# ### Operations
#
# In Python, standard operations are performed pointwise (contrary to Matlab for instance). To do matrix operations, you need to call specific methods (`numpy.matmul` for instance).

# maths: pointwise operations
x = np.array([1, 2, 3, 4, 5]).astype(np.float)
y = np.array([6, 7, 8, 9, 10]).astype(np.float)
print(x*y)
print(y/x)
print(y//x)
print(y%x)
print(x**y)

# +
x[2] = 0.
x[3] = -1.

z = y/x
print(z)
z = np.divide(y, x, where=(x!=0), out=np.full(x.shape, -999, dtype=x.dtype))  # no more warning message
# -

print(z)
w = np.log10(x)
print(w)
w = np.log10(x, where=(x>0), out=np.full(x.shape, -999, dtype=x.dtype))
print(w)

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
xmean = np.mean(x, axis=(0, 1))  # computes mean over the 0 a
print(xmean.shape)

# ## Broadcasting
#
# In order to avoid loops, it is strongly advised to use broadcasting rules (cf. [docs.scipy](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

# broadcasting (https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
x = np.reshape(np.arange(24), (2, 3, 4))

xmean = np.mean(x, axis=0)  # mean over the first dimension
print(xmean.shape, x.shape)
anom = x - xmean    
# works because trailing dimensions (i.e. the last dimensions) are the same

xmean = np.mean(x, axis=-1)
print(xmean.shape, x.shape)
# anom = x - xmean  # doen't work because trailing dimensions are not the same

xmean = np.mean(x, axis=-1, keepdims=True)
print(xmean.shape, x.shape)
anom = x - xmean    
# work because virtual dimensions (1) can be broadcasted

# if you are lazy to remember the broadcasting rules, use the numpy.newaxis method.
y = np.zeros((5, 2, 7, 3, 10, 4))
xnd = x[np.newaxis, :, np.newaxis, :, np.newaxis, :]
print(xnd.shape)
print(y.shape)
z = y * xnd
print(z.shape)

# ## Managing filled values
#

# numpy nans
x = np.arange(1, 10).astype(np.float)
print(x)
x[0] = np.nan
print(x)

i = np.nonzero(np.isnan(x))
print(i) 
i = np.nonzero(x != x) # Mathematical definition of NaN

# Use special functions to handle NaNs
print(np.nanmean(x))
print(np.nansum(x))
print(np.nanstd(x))

# +
# warning: NaNs can only be used with Float arrays (not integer arrays)
x = np.arange(1, 10).astype(np.double)
x[0] = np.nan
print(x)

x = np.arange(1, 10).astype(np.int)
#x[0] = np.nan
# -

# numpy.ma (masked arrays)
x = np.arange(1, 10).astype(np.int)
print(type(x))

x = np.ma.masked_where(x==0, x) # mask data where nan
x = np.ma.masked_equal(x, 5)    # mask x when equal to 5
x = np.ma.masked_greater(x, 7)  # mask x when greater than 7
x = np.ma.masked_less(x, 3)     # mask x when less than 3
x[2] = np.ma.masked  # mask second elements
print(type(x))
print(x)

print(x.mask)    # new attribute as appeared
print(np.ma.getmask(x))  # equivalent to x.mask
print(np.mean(x))  # no more need to do a NaN mean
print(np.sum(x))
print(np.std(x))
print(np.cumsum(x)) 

# warning for masked_arrays
x = np.arange(10, 15).astype(np.float)
x = np.ma.masked_where(np.isnan(x), x)
print(x)
print(x.mask)
iok = np.nonzero(x.mask == False)  #  for unmasked values
print(x[iok])  # returns only first value

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

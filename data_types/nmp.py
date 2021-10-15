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
# - Create multi-dimensional arrays
# - Access array attributes (shape, number of dimensions, data types)
# - Manipulate arrays (changing shape, tiling)
# - Manipulate missing values
# - Perform optimized numerical operations (pointwise or matrix) via broadcasting (no loops)

# ## Array manipulation

# ### Array initialisation

# There are several methods to initialize 1D arrays. `arange` takes an argument a start, end end stride argument.

# +
import numpy as np 

x = np.arange(0, 10, 1) # equivalent to Matlab 0:1:9
x
# -

# `linspace` takes a start, end and a number of elements:

x = np.linspace(10, 20, 41) # 10 to 20 with 41 values
x

# `array` allows to init from `list` for instance:

x = np.array([1, 2, 3, 4, 5]) # initialisation from list 
x

# Initialization of ND arrays can be achieved using different methods, which take as arguments the shape of the array and eventually the type.

x = np.ones((2, 3, 8), dtype=int) # init with 1 integers
x

x = np.zeros((2, 3, 8), dtype=float) # init with 0 floats 
x

x = np.full((2, 3, 8), -99, dtype=float)  # fill array with 10.1
print(x)

# ### Changing data type

# Changing data type is done by using the `astype` function:

x = x.astype(int)  # conversion from floats to int
x

# ### Getting attributes

# Numpy arrays have several attributes. To get the number of dimensions:

x.ndim

# to get the shape:

x.shape

# to get the data type:

x.dtype

# ### Indexing

# Indexing is done as for lists, except that it can be done along several dimensions:

x = np.ones((10, 20, 15, 30), dtype=float)

x[:, :, 0, :].shape


x[:, -1, ::2, ::2].shape

x[:, :, 0:1, ::3].shape

# Using `...`, you can also access an array without fully knowing it's shape:

x[..., 0].shape 

x[..., 2:5, 0].shape 

x[-1, ...].shape

x[::2, ::3,  ...].shape

# `numpy.array` can be used to index `numpy.array`, but prefer using `slice` instead.  Indeed, using the former may be error prone. 
#
# For instance, let's create a 2D array. 

z = np.arange(20 * 10)
z

x = np.reshape(z, (20, 10))
x.shape

# For extracting a subspan of an array, you might want to use:

i = [0, 1, 2, 3]
j = [5, 6, 7, 8]
x[i, j]

# In this case, the output is 1D. It extracts the value for each `(i, j)` pair  and is equivalent to:

x[i[0], j[0]], x[i[1], j[1]], x[i[2], j[2]], x[i[3], j[3]]

# Beside, this will fail if `i` and `j` have different sizes. The proper syntaxt would be:

i = slice(0, 4)
j = slice(5, 9)
x[i,j]

# The values obtained in the first try are the elements in the diagonal of the subspan.

# ### Copy

# As for list, assigment of numpy arrays should not be used to make copies, since the reference is copied, not the values. In the following, the modification of `x` modifies `y`, and conversely:

x = np.arange(10)
y = x
y[0] = -1
x[-1] = 1000
x, y

# To make copies, use the `copy` method:

x = np.arange(10)
y = x.copy()  # deep copy of x into y 
y[0] = -1
x[-1] = 1000
x, y

# ### Reshaping

# If we create a 2D array:

x = np.zeros((6, 4))
for i in range(6):
    x[i, :] = np.arange(4) + i*4
x.shape

# The conversion into 1D can be achieved using `ravel`:

x1dc = np.ravel(x)   # converts ND to 1D following C order
x1dc

# By default, the order of the `reshaping` follows the `C` order. You can specify an Fortran-like order as follows:

x1df = np.ravel(x, order="F")
x1df

# To convert an array from a given set of dimensions to another one, use the `reshape` method. The number of elements in the source and destination shapes must be the same.

xresc = np.reshape(x, (2, 3, 4)) 
xresc

xresf = np.reshape(x, (2, 3, 4), order="F")
xresf

# If we recreate a 3D array as follows:

x = np.reshape(np.arange(2 * 3 * 4), (2, 3, 4))
x.shape

# We can reshape it from ND to 2D, by keeping one dimension unchanged, as follows:

xtest = np.reshape(x, (2, -1))
xtest.shape

# Here,  we keep the first dimension but transform (3, 4) in 12.

xtest2 = np.reshape(x, (-1, 4))
xtest2.shape

# Here, we keep the last dimension but transform (2, 3) in 6.

# ### Repeating along a given dimensions

# To repeat an array along a dimension, use the `tile` function. If we create a 1D array:

x = np.zeros((10, 20, 30))
x.shape

# We can repeat it 40 times as follows:

xtile = np.tile(x, (40, 1, 1, 1))
xtile.shape

# Note that the dimension argument of `tile` must always finish by 1. I.e. the array can only be extended along the first dimensions. If we try to extend the above array along the last dimension as follows:

xtile2 = np.tile(x, (1, 1, 1, 40))
xtile2.shape

# Here the result has the wrong dimension. To make it work, the first syntax must be used with `transpose`:

xtile2 = np.tile(x, (40, 1, 1, 1))
xtile2.shape

xtile2 = np.transpose(xtile2, (1, 2, 3, 0))
xtile2.shape

# ### Changing dimension order

x = np.ones((5, 10, 15))
x.shape

# Changing dimension orders is achieved using the `transpose` method. By default, it reverses the dimensions.

xt = x.T
xt.shape

xt = np.transpose(x) # identical to xt = xt.T
xt.shape

# But you can specify the new order as an argument:

xt = np.transpose(x, (2, 0, 1))
xt.shape

# ### Testing conditions

xresc = np.reshape(np.arange(24), (2, 3, 4))

# Testing conditions can be done by using operators on the array. It returns an array of boolean:

condition = (xresc <= 12) & (xresc >= 3)  # array of boolean (True if condition is met)
condition

# To display the values when the condition is met:

xresc[condition]

# To display the values when condition is not met:

xresc[~condition]

# To get the indexes where the condition is met, use the `nonzero` method. It returns a tuple with the indexes where the condition is met for each axes.

ind = np.nonzero(condition)
ind

# Therefore, the condition is met for `xresc[0, 0, 3]`, `xresc[0, 1, 0]`, `...`, `xresc[0, 2, 3]`, `xresc[1, 0, 0]`

# You can also get the values where condition is met using the indexes:

xresc[ind]

# To extract the unique occurrences in an array, use the `unique` value:

x = np.array([0, 0, 0, 1, 2, 2, 3, 3, 3, 3])
np.unique(x)

# ### Concatenation

# Concatenation of arrays is achieved by usinging the `concatenate` function, which takes as arguments the arrays to concatenate, and the dimension along which to concatenate:

x = np.zeros((2, 3, 5))
y = np.ones((2, 7, 5))
x.shape, y.shape

# To concatenate the arrays along their 2nd dimension:

z = np.concatenate((x, y), axis=1)  
z.shape

# ## Operations using arrays 

# ### Arhtimetical operations
#
# In Python, standard operations are performed pointwise (contrary to Matlab for instance). To do matrix operations, you need to call specific methods (`numpy.matmul` for instance).

x = np.array([1, 2, 3, 4, 5]).astype(float)
x

y = np.array([6, 7, 8, 9, 10]).astype(float)
y

x * y

y / x

y % x

y // x

x**y

# In the above, the `/` operator returns the right value. However, if `x` has 0 values:

x[2] = 0.
x[3] = -1.
x

z = y / x
z

# Here, we have a warning message, and the output array contains an `inf` value. To avoid this, we can use the `divide` method with the `where` and `out` argument. 
#
# The first one specifies the condition when the operation should be applied. 
#
# The second one specifies an output array which will be used to replace missing values. In this case, the default output will be an array of `NaNs` of the same size as `x`.

z = np.divide(y, x, where=(x!=0), out=np.full(x.shape, np.nan, dtype=x.dtype))  # no more warning message
z

# Here, we have no more warnings and `inf` has been replaced by `nan`. The same thing can be applied to other functions such as `log10`:

w = np.log10(x)
w

w = np.log10(x, where=(x > 0), out=np.full(x.shape, np.nan, dtype=x.dtype))
w

# ### Mathematical operations (mean, etc.)

# Here we will work on the given array:

x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [7, 1, 3, 5, 6, 7, 8, 10, 4, 6],
             [5, 1, 0, 3, 5, 8, 12, 5, 8, 1]])
x.shape

# To compute the mean over the entire array:

out = np.mean(x)
out

# To compute the standard deviation over second dimension:

out = np.std(x, axis=1) 
out

# To compute the sum along the first dimension:

out = np.sum(x, axis=0)
out

# Same thing for cumulated sum:

out = np.cumsum(x, axis=0) # compute sum over first dimension
out

# Same thing for product:

out = np.prod(x, axis=0) 
out

# This also works for multi-dimensional arrays:

x = np.reshape(np.arange(24), (2, 3, 4))  # lat, lon, time
x.shape

# To compute the mean along the first and 2nd dimensions:

xmean = np.mean(x, axis=(0, 1))
xmean.shape

# To compute the mean along the 2nd and 3rd dimensions:

xmean = np.mean(x, axis=(1, 2))
xmean.shape

# ## Broadcasting
#
# To make computation, it is highly advised to avoid loops. Numpy provides different broadcasting rules which allow to prevent from using loops (cf. [docs.scipy](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html))

# Imagine that we have a ND array, with the dimensions being `(time, lat, lon)`:

x = np.reshape(np.arange(24), (2, 3, 4))  # time, lat, lon
x.shape

# If we want to compute the anomalies, we first compute the temporal mean:

xmean = np.mean(x, axis=0) 
xmean.shape

# Now we can compute the anomalies

anom = x - xmean
anom.shape

# In this case, the code above works even though the `x` and `xmean` have different shapes. This is because the last two dimensions (i.e. trailing dimensions)  are the same. Now, imagine that the array is in fact ordered as `(lat, lon, time)`.
#
# We first compute the mean over the time-dimensions:

xmean = np.mean(x, axis=-1)    # temporal mean
xmean.shape

# However, the computation of the anomalies will fail:

# +
#anom = x - xmean  
# -

# It fails because the *first* (i.e leading) dimensions are the same, which does not allow broadcasting. This can be fixed by using the `keepdims` argument. It will keep a virtual dimension on the mean output.

xmean = np.mean(x, axis=-1, keepdims=True)
xmean.shape

anom = x - xmean

# If you are lazy to remember the broadcasting rules, you can use the `numpy.newaxis` method to add virtual dimensions. It allows to add degenerated dimensions on an array. If we look at the shape of our `x` array:

x.shape

# If we create a 6D array of dimensions:

y = np.zeros((5, 2, 7, 3, 10, 4))
y.shape

# To multiply `x` and `y` without loops, we can add degenerated dimenions to `x` in order to align them with the dimensions of `y`:

xnd = x[np.newaxis, :, np.newaxis, :, np.newaxis, :]
xnd.shape

# We can see that now the shapes of the `xnd` array and of `y` are aligned:

y.shape

# Now we can multiply both arrays:

z = y * xnd
z.shape

# ## Managing filled values
#
# Filled values are generally defined as `numpy.nan` values.

x = np.arange(1, 10).astype(float)
x[0:3] = np.nan
x

# Checking whether values are `NaN` is achieved by using the `np.isnan` method

cond = np.isnan(x)
cond

# To find the index of the `NaN` values:

np.nonzero(np.isnan(x))

# An equivalent to the `np.isnan` method is to use the mathematical definition of `NaNs`.

np.nonzero(x != x) # Mathematical definition of NaN

# **Warning: `NaNs` can only be used with Float arrays (not integer arrays)**

# ### Operations on filled values
#
# To perform operations on data containing `NaNs` requires the use of special functions:

np.nanmean(x)

np.nansum(x)

np.nanstd(x)

# Since this can be a bit annoying, `numpy.array` objects can be converted into `masked_array` objects, whose operations automatically discards NaN.
#
# ### Masked array

x = np.arange(0, 10).astype(int)
x

# To convert an array into a masked array, the following methods can be used:

x = np.ma.masked_where(x==0, x)
x

x = np.ma.masked_equal(x, 5)
x

x = np.ma.masked_greater(x, 7)
x

x = np.ma.masked_less(x, 3)
x

x = np.ma.masked_where(np.isnan(x), x)
x

x[2] = np.ma.masked
x

# This new object has additional attributes and method. Especially for assessing where the filled values are located.

x.mask

np.ma.getmaskarray(x)

np.mean(x)

np.sum(x)

np.std(x)

# **It is strongly advised to use the `np.ma.getmaskarray` method rather than using the `mask` attribute. Indeed, the latter will return a `bool` instead of an array of `bool` if no data is missing.**

# warning for masked_arrays
x = np.arange(10, 15).astype(float)
x = np.ma.masked_where(np.isnan(x), x)
x


# Therefore, extracting all non missing values from an array is not safe using `mask`:

iok = np.nonzero(x.mask == False) 
x[iok]

# In this case, only the first value is returned, instead of all values.

# However, it works perfectly using the `getmaskarray` method:

iok = np.nonzero(np.ma.getmaskarray(x) == False)
x[iok]

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
# Scipy comes with numerous submodules, which are listed below (source: [scipy.org](https://www.scipy.org/))
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

# ## Loops
#
# As highlighted in the above, it is highly recommended to avoid the use of loops. However, if needed, the looping method in arrays is described below:
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

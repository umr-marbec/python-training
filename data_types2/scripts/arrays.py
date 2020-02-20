import numpy as np

######################################################### Array initialisation
x = np.arange(0, 10, 1) # equivalent to Matlab 0:1:9
x = np.linspace(10, 20, 41) # 10 to 20 with 41 values
x = np.array([1, 2, 3, 4, 5]) # initialisation from list 
x = np.ones((2, 3, 8), dtype=np.int) # init with 1 integers
x = np.zeros((2, 3, 8)) # init with 0 floats 
x = np.empty((2, 3, 8), dtype=np.float) # init with random floats 
x = np.full((2, 3, 8), 10.)  # fill array with 10.
print(x)
x = x.astype(np.int)  # conversion from floats to int

type(x) 
print(x.ndim) 
print(x.shape)
print(x.dtype)

######################################################### array manipulation
x = np.ones((2, 3, 8), dtype=np.float)

####### indexing: same indexing as for lists for any array dimensions
print(x[:, :, 0].shape)
print(x[:, -1, ::2].shape) # (2,3) (2,4) array subspans

####### copies: arrays are mutable, take care copy assignments
x = np.arange(10)
y = x
y[0] = -1
x[-1] = 1000
print(x)
print(y)
print(id(x), id(y))

x = np.arange(10)
y = x.copy()  # copy x array into y variable
y[0] = -1
x[-1] = 1000
print(x)
print(y)
print(id(x), id(y))

#################################### reshaping
x = np.zeros((6, 4))
for i in range(6):
    x[i, :] = np.arange(4) + i*4


x1dc = np.ravel(x)   # converts ND to 1D following C order

# equivalent to:
N = np.prod(x.shape)
output = np.zeros(N)
cpt = 0
for i in range(6):  # starts with first dimensionss
    for j in range(4):
        output[cpt] = x[i, j]
        cpt += 1
print(np.all(output == x1dc))

# Order=Fortran: the order of the loops is reversed (outer dim to inner dim)
x1df = np.ravel(x, order="F")

# equivalent to:
N = np.prod(x.shape)
output = np.zeros(N)
cpt = 0
for j in range(4):  # starts with outer dimension!
    for i in range(6):
        output[cpt] = x[i, j]
        cpt += 1
print(np.all(output == x1df))

print(x1dc)
print(x1df)

## Changing the shape of the array in C order
xresc = np.reshape(x, (2, 3, 4)) #

# equivalent to
xresc_t = np.zeros((2, 3, 4))
temp = np.ravel(x)
cpt = 0        
for i in range(2):
    for j in range(3):
        for k in range(4):
            xresc_t[i, j, k] = temp[cpt]
            cpt += 1

xresf = np.reshape(x, (2, 3, 4), order="F") # reshape following Fortran order

# identical to
cpt = 0
xresf_t = np.zeros((2, 3, 4))
temp = np.ravel(x, order='F')
for k in range(4):
    for j in range(3):   # loop orders are reversed in Fortran order
        for i in range(2):
            xresf_t[i, j, k] = temp[cpt]
            cpt += 1

################################## repeating an array along given dimensions
x = np.arange(10)
xtile = np.tile(x, (2, 1)) # (2 ,10) equivalent to repmat
xtile2 = np.tile(x, (1, 2)) # (1, 20)
print(xtile.shape, xtile)
print(xtile2.shape, xtile2)

######################### changing dimension orders
x = np.ones((5, 10, 15))
xt = np.transpose(x) # identical to xt = xt.T
xt2 = np.transpose(x, (2, 0, 1)) # (15, 5, 10)
print(x.shape)
print(xt.shape)
print(xt2.shape)

############################################### testing on array
x = np.reshape(np.arange(24), (2, 3, 4))
condition = (xresc <= 12) & (xresc >= 3)  # array of boolean (True if condition is met)

# display values where condition is met
print(xresc[condition])

ind = np.nonzero(condition)   # returns a tuple of the i, j, k indexes pairs that match conditions
print(ind)
print(ind[0])  # extracts the i indexes
print(xresc[ind])   # extracts the values that match the condition (1D array)

####################################################### extract unique values
x = np.array([0, 0, 0, 1, 2, 2, 3, 3, 3, 3])
print(np.unique(x))

################################################## concatenation
x = np.zeros((2, 3, 5))
y = np.ones((2, 7, 5))

# concatenates x, y along their second dim. dim[0] and dim[2] must have the same values
z = np.concatenate((x, y), axis=1)  
print(z.shape)

x = np.arange(0,5)
x2d = np.atleast_2d(x)
print(x.shape)
print(x2d.shape)
# magic staff

########################################### saving + loading
np.savez('save.npz', xt2=xt2, x=x)
fin = np.load('save.npz')  # loaded as a dict
xt2 = fin['xt2']
x = fin['x']

######################################### maths
x = np.array([1, 2, 3, 4, 5]).astype(np.float)
y = np.array([6, 7, 8, 9, 10]).astype(np.float)
x*y
y/x
y//x
y%x
x**y

x[2] = 0.
x[3] = -1.

z = y/x
print(z)
z = np.divide(y, x, where=(x!=0), out=np.full(x.shape, -999, dtype=x.dtype))  # no more warning message
print(z)
w = np.log10(x)
print(w)
w = np.log10(x, where=(x>0), out=np.full(x.shape, -999, dtype=x.dtype))
print(w)

x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [7, 1, 3, 5, 6, 7, 8, 10, 4, 6],
             [5, 1, 0, 3, 5, 8, 12, 5, 8, 1]])

np.mean(x, axis=0) # compute mean over first dimension
np.std(x, axis=1) # compute standard deviation over second dimension
np.sum(x, axis=0) # compute sum over first dimension
np.cumsum(x, axis=0) # compute sum over first dimension
np.prod(x, axis=0) # computes the prod along the first dimension


x = np.reshape(np.arange(24), (2, 3, 4))
xmean = np.mean(x, axis=(0, 1))  # computes mean over the 0 a
print(xmean.shape)

########################## broadcasting (https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
x = np.reshape(np.arange(24), (2, 3, 4))

xmean = np.mean(x, axis=0)
anom = x - xmean    
# works because trailing dimensions (i.e. the last dimensions) are the same
print(xmean.shape, x.shape)
print(anom.shape)    

xmean = np.mean(x, axis=-1)
# anom = x - xmean    
# doen't work because trailing dimensions are not the same
print(xmean.shape)
print(x.shape)
print(anom.shape) 

xmean = np.mean(x, axis=-1, keepdims=True)
anom = x - xmean    
# work because virtual dimensions (1) can be broadcasted
print(xmean.shape)
print(x.shape)
print(anom.shape) 

# if you are lazy to remember the broadcasting rules, use the numpy.newaxis method.
y = np.zeros((5, 2, 7, 3, 10, 4))
xnd = x[np.newaxis, :, np.newaxis, :, np.newaxis, :]
print(xnd.shape)
print(y.shape)
z = y * xnd
print(z.shape)

################################################# numpy nans

x = np.arange(1, 10).astype(np.float)
print(x)
x[0] = np.nan
print(x)
i = np.nonzero(np.isnan(x))
i = np.nonzero(x != x) # definition of NaN
print(i) 

# Use special functions to handle NaNs
np.nanmean(x)
np.nansum(x)
np.nanstd(x)

#warning: NaNs can only be used with Float arrays (not integer arrays)
x = np.arange(1, 10).astype(np.double)
x[0] = np.nan

#x = np.arange(1, 10).astype(np.int)
#x[0] = np.nan

################################################# numpy.ma (masked arrays)
x = np.arange(1, 10).astype(np.int)
print(type(x))
x = np.ma.masked_where(x==0, x) # mask data where nan
x = np.ma.masked_equal(x, 5)    # mask x when equal to 5
x = np.ma.masked_greater(x, 7)  # mask x when greater than 7
x = np.ma.masked_less(x, 3)     # mask x when less than 3
x[2] = np.ma.masked  # mask second elements

print(type(x))  # type of x has changed
print(x)
print(x.mask)    # new attribute as appeared
print(np.mean(x))
print(np.sum(x))
print(np.std(x))
print(np.cumsum(x)) 


################################################# warning for masked arrays

# warning for masked_arrays
x = np.arange(10, 15).astype(np.float)
x = np.ma.masked_where(np.isnan(x), x)
print(x)
print(x.mask)
iok = np.nonzero(x.mask == False)  #  for unmasked values
print(x[iok])  # returns only first value

print(np.ma.getmask(x))  # one single value (False) if all the array is unmasked
print(np.ma.getmaskarray(x))   # match the size of the input array
iok = np.nonzero(np.ma.getmaskarray(x) == False)  #  for unmasked values
print(x[iok])  # returns all the values

# to force an element to be masked
x[2] = np.ma.masked
print(np.ma.getmask(x)) 
print(np.ma.getmaskarray(x))

############################################## saving masked array,
# convert them back to numpy arrays with NaNs when masked
# conversion of masked values into NaN
x[np.ma.getmaskarray(x)] = np.nan
# conversion from np.ma.array to np.array
x = np.array(x)
# saving into file
np.savez("zarray.npz", x=x)





# loading the numpy library
import numpy
numpy.abs(-5) # calling numpy function abs

# loading matplotlib with the shortname mp
import matplotlib as mp
mp.is_interactive()  # calling matplotlib function is_interactive

# loading the DataFrame function of the pandas lib.
from pandas import DataFrame
DataFrame() # no panads.DataFrame in this case

# loading all the functions of the scipy.stats lib.
# UNADVISED!!!!!
from scipy.stats import *
randint(0, 1) # no scipy.stats.randint in this case

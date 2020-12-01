# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Text files
#
# ## Opening files
#
# To open file a text file, use the `with` statement. It allows to insure that the file is properly opened and properly closed, even if an error is encountered (see [the-with-statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) for a detailed description).

# +
# defining the name of the file to read
filename = 'data/nao.txt'

with open(filename,'r') as f:
    print(f.closed)
print(f.closed)
# -

# ## Reading

# read all the lines and store them in a list
with open(filename,'r') as f:
    lines = f.readlines()
print(len(lines))
print('@%s@' %lines[0])
print('#%s#' %lines[0].strip())  # removes the \n char

# Read all the file and store as 1 string
with open(filename,'r') as f:
    data = f.read()
print(len(data))
print(data[:10])

# Read the first 200 chars of the file and store as 1 string
with open(filename,'r') as f:
    data = f.read(200)
print(len(data))
print(data)

# loop over all the lines of the file, and extract the first one
# finishes when "end of line is found"
with open(filename,'r') as f:
    for line in f:
        print(line.strip())

# to parse a certain range of the file, one 
# way is to use the itertools package
import itertools
with open(filename,'r') as f:
    for line in itertools.islice(f, 5, 10):
        print(line.strip())

# ## Writting
#
# Files are written out line by line.

# +
# Generates some data
import numpy as np

xdata = np.linspace(0, np.pi/4., 5)
cosx = np.cos(xdata)
sinx = np.sin(xdata)
tanx = np.tan(xdata)
# -

# opening the file
with open('data/outfile.txt', 'w') as fout:

    # writting the header: 4 strings separated by tabs.
    header = ['x', 'cos', 'sin', 'tan']
    string='%s\t%s\t%s\t%s\n' % (header[0], header[1], header[2], header[3])  # writes the header
    print(string)
    fout.write(string)


    # looping over all the data
    for x, c, s, t in zip(xdata, cosx, sinx, tanx):
        # writting the string associated with the data
        string = '%.4f\t%.8f\t%.8f\t%.8f\n' %(x, c, s, t)    # writes the data
        print(string)
        fout.write(string)

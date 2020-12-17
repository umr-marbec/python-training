# ---
# jupyter:
#   jupytext:
#     formats: py
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

# ## Loops
#
# ### Definition
#
# Loops should be used when a set of actions should be repeated a certain number of times (for instance on each element of a list).
#
# There is mainly two ways to perform a loop: by using a ```for``` statement, or by using a ```while``` statement.
#
# ### Loops in Python
#
# In Python, the general structure of a loop is:
#     
#     for v in iterable:
#         action
#
#     while(condition):
#         action
#     
# <div class="alert alert-info">
#     You can always replace a <i>for</i> loop by a <i>while</i> loop, and conversely. 
# </div>
#

# +
# creates a list
x = range(1, 11)

# loop using the list index
for p in range(0, len(x)):
    print('index ', p, 'value', x[p])  # p: index of the element
# -

# loop using the list elements (works for iterables, such as list, tuples)
for v in x:
    print(v)  # temp: element itself

# loop using the list elements (works for iterables, such as list, tuples)
for v in x[::-1]:
    print(v)  # temp: element itself

# pairwise loops
# to be used when looping using indexes
x = range(1, 10)[::-1]
y = range(11, 20)
for i, j in zip(x, y):
    print(i, j)
# x[0], y[0]
# x[1], y[1]
# x[2], y[2] ...

# pairwise loops: stops when reaches one list end.
x = range(1, 3)[::-1]
y = range(11, 20)
for i, j in zip(x, y):
    print(i, j)

# +
# any for loop can be converted into while loop, and conversely
x = range(1, 10)

p = 0
while p<len(x):
    print('index ', p, 'value', x[p])  # p: index of the element
    p += 1 # iteration of counter
        
p = len(x) - 1
while (p>= 0):
    print('index ', p, 'value', x[p])  # p: index of the element
    p -= 1 # iteration of counter 
# -

for i in range(0, 2):
    for j in range(0, 3):
        for k in range(0, 1):
            print('i', i, 'j', j, 'k', k)

# +
# Loop comprehension: loops writen in one single line
combs1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] 
print(combs1)

# equivalent to (but much shorter and more elegant)
combs2 = [] 
for x in [1, 2, 3]:
    for y in [3, 1, 4]: 
        if x != y:
            combs2.append((x, y))
print(combs2)

# +
x = range(1, 10) 
y = [3, 5, 6] 

# loop over the elements of x and add them to the output list
# if they are not in y
# 3, 5, 6 are not
z = [temp for temp in x if temp not in y] 
print(z)
# -

# Break: leaves the loop when condition is met
for p in range(0, 10):
   
    print('===== ', p)
    
    if(p > 3):
        break

# Continue: skip the end of the block when condition is met
for p in range(0, 10):

    print('++++++ ', p)

    if(p > 3):
        continue

    print('below')

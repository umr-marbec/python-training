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

# # Loops
#
# ## Definition
#
# Loops should be used when a set of actions must be repeated a certain number of times (for instance on each element of a list).
#
# There is mainly two ways to perform a loop: by using a ```for``` statement, or by using a ```while``` statement.
#
# ## Loops in Python
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

# First, let's create a list, which is an iterable

# creates a list
x = ['a', 'b', 'c', 'd', 'e']
x

# You can loop over a list by using its `index` as follows:

# loop using the list index
for p in range(0, len(x)):
    print('iterable ', p, 'element', x[p])

# Here, the iteration is done on an integer (`p`), which is an integer.

# But the iteration can also be performed on the elements themselves:

# loop using the list elements (works for iterables, such as list, tuples)
for v in x:
    print('iterable ', v)  # temp: element itself

# ## Pairwise loops
# There is the possiblity to loop simultaneously over different elements using the `zip` method, which returns a `tuple` of pairs.

x = ['a', 'b', 'c', 'd']
x

y = ['w', 'x', 'y', 'z']
y

list(zip(x, y))

for i, j in zip(x, y):
    print(i, j)

# The `zip` method method will stop when the end of one of the iterable has been reached.

z = ['alpha', 'beta']

for val in zip(x, y, z):
    print(val)

# Any for `loop` can be converted into a `while` loop, and conversely. For instance, to navigate on a list:

# +
# any for loop can be converted into while loop, and conversely
x = ['a', 'b', 'c', 'd']


p = 0
while p < len(x):
    print('index ', p, 'value', x[p])  # p: index of the element
    p += 1 # iteration of counter
# -

# To navigate in a list starting by the end:

p = len(x) - 1
while (p >= 0):
    print('index ', p, 'value', x[p])  # p: index of the element
    p -= 1 # iteration of counter 

# ## Imbricated loops
#
# Imbricated loops are achieved by indenting the code as many times as necessary

for i in range(0, 2):
    for j in range(0, 3):
        for k in range(0, 1):
            print('i', i, 'j', j, 'k', k)

# ## Loop comprehension
#
# Python allows writting loops in a very synthetic way, which is called *loop comprehension.* For instance, the following loop:

# equivalent to (but much shorter and more elegant)
combs2 = [] 
for x in [1, 2, 3]:
    for y in [3, 1, 4]: 
        if x != y:
            combs2.append((x, y))
combs2

# can be written as follows:

combs1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y] 
combs1

# If you have 2 lists, `x` and `y`:

x = list(range(1, 10))
y = [3, 5, 6] 
list(x)

# If you want to extract the element of `x` which are not contained in `y`:

z = [a for a in x if a not in y] 
z

# ## Loop controls: break and continue
#
# `break` allows to leave a `loop` when a condition is met:

# Break: leaves the loop when condition is met
for p in range(0, 10):
   
    print('===== ', p)
    
    if(p > 3):
        break

# On the other hand, `continue` does not leave the loop but the statements that come after are not reached.

# Continue: skip the end of the block when condition is met
for p in range(0, 10):

    print('++++++ ', p)

    if(p > 3):
        continue

    print('below')

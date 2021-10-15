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

# # Code blocks
#
# In Python, **conditional statements, functions and loops** are defined within **code blocks**, which have in common:
#
# - The block definition must end with `:`
# - The code inside the block must be *indented to the right*
# - When leaving the block, the code  *must be indented to the left*
#
# **There is no begin/end statements, everything is handled by the indent**
#
# <div class="alert alert-danger">
#     <b>Common errors</b>
#     <br>
#     Indent issues are very common at the beginning, be carefull
# </div>
#
#
# <div class="alert alert-warning">
#         <b>Text Editor issues</b>
#      <br>
#     With some text editors, the <i>tab</i> keys would make your code incompatible with other systems.
# Use 4 spaces instead.
# </div>
#
# # Conditional statements
#
# ## Definition
#
# Conditional statements allow to perform predifined actions depending on certain conditions. 
#     
# ##  Defining conditional statements
#
# The general structure of a conditional statement is:
#
# ```
# if(cond1):
#     action1
# elif(cond2):
#     action2
# else:
#     action3
# ```

# +
x = -10
y = -11
z = -12

# Care with the indent
if ((x==y) & (x==z)):
    print('Equality')
elif ((x <= y) & (y <= z)):
    print('Increasing order')
elif((x >= y) & (y >= z)):
    print('Decreasing order')
else:
    print('No order')
# -

# The use of brackets in not always necessary:

# +
x = ['a', 'b', 'c']


if 'a' in x:
    print('a in list')
else:
    print('a not in list')
    
if ('z' in x):
    print('z in list')
else:
    print('z not in list')
# -

# There is the possibility to write conditional statements in one line: 

# possibility to write if statements in one line
print('a in list') if 'a' in x else print('a not in list')
print('z in list') if 'z' in x else print('z not in list')
if('a' in x): print('match')

# For imbricated conditions, the code need to be indented one extra time. **Again, carefull with the indent.**

x = y = -10
if(x == y):
    # starts a new block with new conditional testing
    if(x > 0):
        print('x == y and positive')
    else:
        print('x == y and negative')


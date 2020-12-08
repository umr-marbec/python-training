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

# ## Numerics
#
# ### Comparisons
#
# The following expressions can be used to compare numerical values (source: [python3](https://docs.python.org/3/library/stdtypes.html))
#
# | Python expression | Meaning    
# |:-----------------:|:-----------------------:
# | ```not(a)```      | not a
# | ```a == b```      | a equal b 
# | ```a != b```      | a not equal b
# | ```a & b```      | a and b
# | ```a \| b```      | a or b
# | ```a >= b```      | a greater equal b
# | ```a > b```       | a greater b
# | ```a <= b```      | a less equal b
# | ```a < b```       | a less b
#
# ### Operations
#
# Binary operations are listed below (source: [python3](https://docs.python.org/3/library/stdtypes.html))
#
# |Python expression               | Meaning
# |:------------------------------:|:-------------------------------------:
# | ```x + y```                    | sum of x and y
# | ```x - y```                    | difference of x and y
# | ```x * y```                    | product of x and y
# | ```x / y```                    |quotient of x and y
# | ```x // y```                   |floored quotient of x and y
# | ```x % y```                    |remainder of x / y
# | ```-x```                       | x negated
# | ```abs(x)```                   | absolute value or magnitude of x
# | ```complex(re, im)```          | a complex $math re + i\times im$
# | ```c.conjugate()```            | conjugate of the complex number c
# | ```divmod(x, y)```             | the pair ```(x // y, x % y)```
# | ```pow(x, y)```                | x to the power y
# | ```x ** y```                   | x to the power y

x = 13
y = 5

print(x / y)  # division
print(x // y) # floored quotient
print(x % y)  # rest
print(divmod(x, y))

print(pow(x, y))
print(x**y)

# +
c = complex(x, y)
print(c)
print(c.real)
print(c.imag)

cc = c.conjugate()
print(cc)

print(c * cc)
print(abs(c))

# +
x = 11
print(x)

# x = x + 1
x += 1
print(x)

x *= 2 
# x = x * 2
print(x)

# x = x / 3
x /= 3
print(x)

# x = x - 2
x -= 2
print(x)

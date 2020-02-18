x = 1  # int
x = 'string'  # string
x = 2.3  # float
type(x)  # class of the object
dir(x)  # list of methods/attributes
help(x)  # help about methods

x = 'string'
x[0] = 1

x = [0, 1, 2]
y = x 
print('x = ', x, 'y = ', y)
x[1] = 'oups'
print('x = ', x, 'y = ', y)
print(id(x), id(y))

x = [0, 1, 2]
print(id(x))
x.append(1)
print(id(x))

x = [0, 1, 2]
y = x.copy()
print('x = ', x, 'y = ', y)
x[1] = 'oups'
print('x = ', x, 'y = ', y)

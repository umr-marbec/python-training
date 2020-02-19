x = 10
y = 9
z = 10

# Care with the indent
if ((x==y) & (x==z)):
    print('Equality')
elif ((x <= y) & (y <= z)):
    print('Increasing order')
elif((x >= y) & (y >= z)):
    print('Decreasing order')
else:
    print('No order')
    

x = ['a', 'b', 'c']
if 'a' in x:
    print('a in list')
else:
    print('a not in list')
    
if 'z' in x:
    print('z in list')
else:
    print('z not in list')

# possibility to write statements in one line
print('a in list') if 'a' in x else print('a not in list')
print('z in list') if 'b' in x else print('z not in list')
if('a' in x): print('match')

# Warning if you define some variables inside a block and not in another block
x = y = 10
if(x == y): 
    z = 20
else:
    w = 10
print(z)
print(w)

x = y = -10
x = 10
y = -12
if(x == y):
    # starts a new block with new conditional testing
    if(x > 0):
        print('x == y and positive')
    else:
        print('x == y and negative')
else:
    print('x and y are different')

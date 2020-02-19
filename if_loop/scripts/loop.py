# creates a list
x = list(range(1, 11))

# loop using the list index
for p in range(0, len(x)):
    print(p, x[p])  # p: index of the element

# loop using the list elements (works for iterables, such as list, tuples)
for v in x:
    print(v)  # temp: element itself
    
# pairwise loops
x = range(1, 10)
y = range(11, 20)
for i, j in zip(x, y):
    print(i, j)


# any for loop can be converted into while loop, and conversely
cpt=0
while cpt<len(x):
    print(cpt, x[cpt])
    cpt += 1 # iteration of counter 
    
cpt = len(x) - 1
while (cpt>= 0):
    print(cpt, x[cpt])
    cpt -= 1 # iteration of counter 

for i in range(0, 2):
    for j in range(0, 3):
        for k in range(0, 1):
            print('i', i, 'j', j, 'k', k)

# Loop comprehension: loops writen in one single line
combs1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] 
print(combs1)

# equivalent to:
combs2 = [] 
for x in [1, 2, 3]:
    for y in [3, 1, 4]: 
        if x != y:
            combs2.append((x, y))
print(combs2)
        
x = range(1, 10) 
y = [3, 5, 6] 

# loop over the elements of x and add them to the output list
# if they are not in y
z = [temp for temp in x if temp not in y] 
print(x)
print(y)
print(z)

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


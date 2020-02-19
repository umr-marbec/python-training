string1 = 'char1 char2 char3'
len(string1)  # length of a string

chars = list(string1) # returns a list of char

############################## change case
# sets the string to lower case
stringl = string1.lower()
print(stringl)

# sets the string to uper case
stringu = string1.upper()
print(stringu)

stringc = string1.capitalize()
print(stringc)

# note here that syntax is different from list
# output of the method is a new string object since strings are immutable

############################### string manipulation

string2 = string1.replace('Char2', 'toto')
print(string2)

words = string1.split(' ') #['Char1', 'Char2', 'Char3']
print(words)

words = string1.split(',') #['Char1', 'Char2', 'Char3']
print(words)

sep = ',\t'
# merges a list of strings in one string providing a separator
string3 = sep.join(['toto1', 'toto2','toto3'])
print(string3)

string4 = 2 * 'toto1' + '\t' + 'toto2' + \
          '\n' + 'toto3 ' + str(10)
print(string4)  # strings behaves  list

# variables to display
x = 10; y = 0.5; z = 0.005
# string formatting. There should be as many %s as variables to display
string5 = '%04d, %.5f, %.3e\n' %(x, y, z) 
print(string5)

# If you want to write percentage symbol, use %s (string format)
string5 = 'Percentage:\n%d%s' %(x, '%') 
print(string5)

# removing trailing whitespace (usefull when reading a file)
string6 = string5.strip()
print(string6)

######################################### Regular expressions
# allows to match any patterns in a string

# load the regular expression package
import re 

string1 = '2-start'
string2 = 'end-3'

# match string that starts (^) with a number ranging from 0 to 9
pattern1 = '^[0-9]'
reg1 = re.compile(pattern1)

# match string that ends ($) with a number ranging from 0 to 9
pattern2 = '[0-9]$'
reg2 = re.compile(pattern2)

reg1.match(string1)  # match: returns a re.Match object
reg2.match(string2)  # no match: returns None
reg2.match(string1)
reg1.match(string2)

if(reg1.match(string1)):
    print('match')
else:
    print('no match')

# How to split this string into the three names?    
string1 = 'lala     toto                     titi'
string1.split(' ')
reg = re.compile(' +')  # split based on regular expressions
reg.split(string1)    

# full list is to be found here: https://docs.python.org/fr/2.7/howto/regex.html

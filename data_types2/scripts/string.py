string1 = 'this is \t.'
print(string1)
string2 = r'this is \t.'  # \t is escaped since r is added before string def.
print(string2)

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

# note that \

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

string1 = r'2-start'
string2 = r'end-3'

# match string that starts (^) with a number ranging from 0 to 9
pattern1 = r'^[0-9]'
reg1 = re.compile(pattern1)  # ccreates an object that will be used to match string

# match string that ends ($) with a number ranging from 0 to 9
pattern2 = r'[0-9]$'
pattern2 = r'\d$'
reg2 = re.compile(pattern2)

reg1.match(string1)  # match: returns a re.Match object
reg2.match(string2)  # no match: returns None
reg2.match(string1)
reg1.match(string2)

# note: you should compile a regular expression if will be
# often tested. For isolated cases, you can use:
re.match(pattern1, string1)

# to get the integer value, use the groups method of the re package
# use () to encompass the elements you want to extract
pattern1 = r'^([0-9]+)-([a-z]+)$'  # + = 1 or more match of the preceding pattern
pattern2 = r'^([0-9]+)-([a-zA-Z]+)$'  # + = 1 or more match of the preceding pattern
pattern3 = r'^([0-9]*)-([a-zA-Z]+)$'  # * = 0 or more match of the preceding pattern
pattern4 = r'^([0-9]?)-([a-zA-Z]+)$'  # ? = 0 or 1 match of the preceding pattern
reg1 = re.compile(pattern1)
reg2 = re.compile(pattern2)
reg3 = re.compile(pattern3)
reg4 = re.compile(pattern4)

string1 = r'2-start'
string2 = r'04304-end'
string3 = r'04304-END'
string4 = r'-END'

match = reg1.match(string1)
match = reg2.match(string3)
match = reg3.match(string3)
match = reg3.match(string4)
if(match): print(match.groups())

if(match):
    print('match')
    groups = match.groups()
    print(groups)
else:
    print('no match')

# How to split this string into the three names?    
string1 = r'lala     toto                     titi'
string1.split(' ')
reg = re.compile(' +')  # split based on regular expressions: splits with separator = 1 or more spaces
reg.split(string1)    

string1 = r'01 0304 02 45 509 2950 204' # 302 01 2030 39393 50505 s0304 43df'

# list all the digits of the string
reg = re.compile(r'[0-9]')
print(string1)
print(reg.findall(string1))

# List all the 2 to 3 digits. However, 0304 is matched as 030
reg = re.compile(r'[0-9]{2,3}')
print(string1)
print(reg.findall(string1))

# better but 0304 is still matched as 304, and 204 is not matched
reg = re.compile(r'[0-9]{2,3} ')
print(string1)
print(reg.findall(string1))

# we are close with or statements, but there are white spaces
reg = re.compile(r' [0-9]{2,3} |^[0-9]{2,3} | [0-9]{2,3}$')
print(string1)
print(reg.findall(string1))

reg = re.compile(r'\b[0-9]{2,3}\b')   # \b stands for word delimiter
print(string1)
print(reg.findall(string1))



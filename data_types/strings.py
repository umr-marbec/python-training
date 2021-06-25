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

# # Strings
#
# ## Usage
#
# String objects are very common in Python. They are especially usefull when reading and writting text files.
#
# They are defined between simple quotes (```'```) or double quotes (```"```). 
#
#
# <div class="alert alert-warning">     
# <strong>Caution!</strong> Opening and closing quotes must be the same
# </div>
#     
# # Special characters 
#  
# Python contains a set of predefined characters, which are listed below (source: [python.org](https://docs.python.org/3/reference/lexical_analysis.html))
#
# |Character |  Definition    
# |:--------:|:------------------------------:
# |```\a```  | ASCII Bell (BEL)
# |```\b```  | ASCII Backspace (BS)
# |```\f```  | ASCII Formfeed (FF)
# |```\n```  | ASCII Linefeed (LF)
# |```\r```  | ASCII Carriage Return (CR)
# |```\t```  | ASCII Horizontal Tab (TAB)
# |```\v```  | ASCII Vertical Tab (VT)
#
# In order to escape these special characters, add ```r``` before the 1st quote:

str1 = '@this is \n@'  # \n interpreted as line break
print(str1)
str2 = r'%this is \n%'
print(str2)

# ## String manipulation
#
# String objects have a lot of methods to manipulate them. 
#
# Since they are *immutable*, these methods return new string objects, compared to list methods, which
# change the list content.

# ### Extracting characters

# +
string1 = 'char1 char2 char3'
print(len(string1))  # length of a string

chars = list(string1) # returns a list of char
print(chars)
# -

# ### Changing case

# +
# change case
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
# -

# ### Replacement and word splitting

# +
string2 = string1.replace('Char2', 'toto')
print(string2)

words = string1.split(' ') #['Char1', 'Char2', 'Char3']
print(words)

words = string1.split(',') #['Char1', 'Char2', 'Char3']
print(words)
# -

# ### String formatting

sep = ',\n'
# merges a list of strings in one string providing a separator
string3 = sep.join(['toto1', 'toto2','toto3'])
print(string3)

# strings behaves  list, no maths with lists! 
# # + and * for string concatenations
string4 = 2 * 'toto1' + '\t' + 'toto2' + \
          '\n' + 'toto3 ' + str(10)
print(string4)  

# +
# variables to display
x = 10
y = 0.5
z = 0.005

# string formatting. There should be as many %s as variables to display
string5 = '%04d, %.5f, %.3e\n' %(x, y, z) 
# string5 = '%04d, %.5f\n' %(x, y, z) # fails because inconsistent number of var.
print(string5)
# -

# If you want to write percentage symbol, use %s (string format)
string5 = 'Percentage:\n%d%s' %(x, '%') 
print(string5)

string5 = ' test string   '
# removing trailing whitespace (usefull when reading a file)
string6 = string5.strip()
print('#' + string5 + '#')
print('#' + string6 + '#')

# ## Regular expressions
#
# A very powerfull feature is the use of *regular expressions, which allows to match strings with given patterns ([re](https://docs.python.org/3/library/re.html) library).

# ### Creating regular expressions

# +
# load the regular expression package
import re 

# match string that starts (^) with a number ranging from 0 to 9
pattern1 = r'^[0-9]'
reg1 = re.compile(pattern1)  # creates an object that will be used to match string

# match string that ends ($) with a number ranging from 0 to 9
pattern2 = r'\d$'  # \d is a shortcut for [0-9]
reg2 = re.compile(pattern2)  # creates an object that will be used to match string
# -

# ### Matching regular expressions

string1 = r'2-start'
string2 = r'end-3'

reg1.match(string1)  # match: returns a re.Match object

reg2.match(string2)  # no match: returns None

reg2.match(string1)  # returns None (no match)

reg1.match(string2)  # returns a re.Match oject

# note: you should compile a regular expression if will be
# often tested. For isolated cases, you can use:
re.match(pattern1, string1)

# ### Extracting values
#
# To extract the values matched by a regular expression, use the `groups` method. For that, the 
# string pattern that must be extracted must be contained between `()`.

string1 = r'2-start'
string2 = r'04304-end'
string3 = r'04304-END'
string4 = r'-END'


# Function that returns the groups if a match is not None
def test(match):
    if(match):
        print(match.groups())
    else:
        print('none')


# +
# to get the integer value, use the groups method of the re package
# use () to encompass the elements you want to extract
pattern1 = r'^([0-9]+)-([a-z]+)$'  # + = 1 or more match of the preceding pattern
reg1 = re.compile(pattern1)

test(reg1.match(string1)) # Match 
test(reg1.match(string2)) # Match
test(reg1.match(string3)) # No match (end not of the right case)
test(reg1.match(string4)) # No match (doesnt start with num.)

# +
pattern2 = r'^([0-9]+)-([a-zA-Z]+)$'  # + = 1 or more match of the preceding pattern
reg2 = re.compile(pattern2)

test(reg2.match(string1)) # Match 
test(reg2.match(string2)) # Match
test(reg2.match(string3)) # Match (pattern is now case insensitiv)
test(reg2.match(string4)) # No match (doesnt start with num.)

# +
pattern3 = r'^([0-9]*)-([a-zA-Z]+)$'  # * = 0 or more match of the preceding pattern
reg3 = re.compile(pattern3)

# All matches
test(reg3.match(string1))
test(reg3.match(string2))
test(reg3.match(string3))
test(reg3.match(string4))
# -

pattern4 = r'^([0-9]?)-([a-zA-Z]+)$'  # ? = 0 or 1 match of the preceding pattern
reg4 = re.compile(pattern4)
test(reg4.match(string1))  # Match
test(reg4.match(string2)) # No match (more that 0 or 1 number at the begining)
test(reg4.match(string3)) # No match (more that 0 or 1 number at the begining)
test(reg4.match(string4))

# ### Splitting using regular expressions

# How to split this string into the three names?    
string1 = r'lala     toto                     titi'
sp1 = string1.split(' ')
print(sp1)
reg = re.compile(' +')  # split based on regular expressions: splits with separator = 1 or more spaces
sp2 = reg.split(string1) 
print(sp2)

# +
string1 = r'01 0304 02 45 509 2950 204' # 302 01 2030 39393 50505 s0304 43df'

# list all the digits of the string
reg = re.compile(r'[0-9]')
print(string1)
print(reg.findall(string1))
# -

# List all the 2 to 3 digits. However, 0304 is matched as 030
reg = re.compile(r'[0-9]{2,3}')
print(string1)
print(reg.findall(string1))

# better but 0304 is still matched as 304, and 204 is not matched
reg = re.compile(r'[0-9]{2,3} ')  # adding white space at the end
print(string1)
print(reg.findall(string1))

# we are close with or statements, but there are white spaces
reg = re.compile(r' [0-9]{2,3} |^[0-9]{2,3} | [0-9]{2,3}$')
print(string1)
print(reg.findall(string1))

# Solution: use the \b (word delimiter)
reg = re.compile(r'\b[0-9]{2,3}\b')
print(string1)
print(reg.findall(string1))

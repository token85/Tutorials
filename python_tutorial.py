# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:42:56 2019

@author: token
"""
### Help
help(str)


### Numbers

# Integer number example
print(3)

# value type
type(33)

# Float example
print(3.14)

# complex numbers
# "j" sign and parenthesis
x = (15 + 5j)

# check datatype
type(x)


### Strings

'Hello Wordld'

# or

"Hello World"

# String concatenation and variables
a = "Hello "
b = "World"
c = a+b

print(c)

# is is eqwual to:
print("Hello "+'World')


# string multiplication
"Hello World! " * 3

# Substring from left. Numbers from 0
"Hello World! "[1]
"Hello World! "[6:12]
# or
var = "Sample text"
var[7]

# Substring from right
"Hello World! "[-5]


### Operators

# Arithmetical
# use +, -, *, /

# sum 
4 + 2 + 12.2

# multiplication
x = 5 * 5
x

# devide
5 / 2

# devide withot rest
51 // 2

# rest from division
7 % 3

# power
10 **2

# Other way to use arithetical operators - Assignment
x = 17
x += 2
x

# example with power
x = 12
x **= 2
x

# Example with string walue
#
x = []
x += "Hello World"
x

### Variables and datatpes
# Variable name cannot start from number
# upper and lower case are important 
# You can use a-z, 0-9 and "-"
# don't use pyhon command to name variables


# Check datatype
# variable with string datatype
x  = "Python"
type(x)

# variable with list datatype
x = []
type(x)

# variable with float datatype
x = 123.890
type(x)

## Data collections

# Tuples
# Tuple can handle values with different datatype
# Tuple cannot be sort
x = 12, "Python", 0.123, (12+5j), (1,2,3,4,5,6)
type(x)

# You can index tuple elements. Index numbers start from 0 value
x[2]
x[0]

# You can also start from right
x[-1]

# 
x[-1][3]

# Adding new values to tuple. "," is needed
y = 'Hello World !',
z = x + y
z

# Tuple multiplication
z * 3


# Checking index number of tuple elements
z.index("Python")
# index will return index of value first occurence
(z*3).index("Python")

# Count occurence of tuple element
z.count("Python")
# or
(z*3).count("Python")
























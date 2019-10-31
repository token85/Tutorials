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

## Tuples
# Tuple can handle values with different datatype
# Tuple cannot be sort
# Podstawowym typem danych złozonych są krotki. Tworzy się je za pomocą nawiasu okrągłego (). Przetrzymują one uporządkowane dane (kazdemu elementowi przypisany jest unikalny indeks  i∈{0,…,n−1}  gdzie  n∈N  jest liczebnością kolekcji) dowolnych typów:
# You cannot modify list elements
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

# number of tuple elements
len(z)

# Sum, min, max on tuple elements, when tuple have only numeric values
a = (1, 2, 3.14, 8)
# min
min(a)
# max
max(a)
# sum
sum(a)


## Python lists
# Podobnie jak krotki listy przechowują uporządkowane elementy dowolnego typu. Elementy te mogą się też powtarzać. Listy wykorzystują też wszystkie metody dostępne dla krotek. Tworzy się je za pomocą nawiasu kwadratowego:

l = [1, 2, 'Python', "Learn more"]
type(l)

# You can modify list elements
l[2] = 'abc'
l

# You can index list elements. Index numbers start from 0 value
l[2]
l[0]

# You can also start from right
[-1]

# You can add new values
m = l + [1,2,3,4]
m

# or
l.append("New string value")
l

# Choose element from list
l[-2]

# Choose list elements
l[0:3]

# You can change more than one element
l[0:2] = [1,2,3,4,5,6]
l

# Remove list element using list value
l.remove('Learn more')
l

# Delete list elements using index number
del(l[1:2])
l
# Sort list elements
l.sort
l

# Sort list descending
n = [1,5,2,6,8,3.14]
n.sort(reverse=True)
n

# List elements generator. List of values from 0 to 99
o = list(range(1,100))
o

## Sets in Python
# You can create set using {}.
# Set can contain values of different datatypes
# Elements cannot be repeated
# Elements order is not important
# You cannot sort or index sets

# Create set
x = {1,2,3,4,1,2,3,4,"Hello World", "Python", "Python",1,2,3,4}
x

# You can add new elements to set
x.add(987)
x

# You can remove elements from set
x.remove(987)
x

## Dictionaries in Python
# Key-value datatype 
# Keys need to be uniqe
# Dicts have keys, not indexes
# You can kreate keys also using string values
d ={1:"Python", 2:"is", 3:"the", 4:"best", 7: "programming", 9:"language"}
d

# Choosing value using key number
d[1]
d[9]

# You can modify value using key
d[1] = "Python 3"
d

# You can delete value
del d[7]
d

# You can list keys
d.keys()
# # #  Out[107]: dict_keys([1, 2, 3, 4, 9])

# You can list values
d.values()
# # # Out[108]: dict_values(['Python 3', 'is', 'the', 'best', 'language'])

## zip() function can join different type of collection

my_tuple = 12, "Python", 0.123, (12+5j), (1,2,3,4,5,6)
my_list = [1, 2, 'Python', "Learn more"]
my_set = {1,2,3,4,1,2,3,4,"Hello World", "Python", "Python",1,2,3,4}
my_dict = {1:"Python", 2:"is", 3:"the", 4:"best", 7: "programming", 9:"language"}


# You can reate list using zip() function
zip_list = list(zip(my_tuple, my_list, my_set, my_dict))
zip_list

# You can create dict using zip() function
a=(1,2,3)
b=("Hello","Python","!")
zip_dict = dict(zip(a,b))
zip_dict

### if statement in Python
# You need use ":" in condition line
# use 4 space before result code
# use == if you want use equal condition
x = 100

if x > 100:
    print("Better than 100")
elif x == 100:
    print("x is 100")
elif x < 100:
    print("x is less then 100")
else:
    print("Never mind")


# Conditional statements
x = 10.1
print(x, 'is', 'greater than 100' if x > 100 else 'is not greater than 100')


### For loop
# numbers from 0 to 99
for i in range(100):
    print("number: " + str(i))

# numbers from 1 to 100
for i in range(100):
    print("number: " + str(i+1))

### While loop

n = 10
while n < 101:
    print("current number: ", n)
    n += 2
    

# using break, if you want to quit while loop ealier
n = 10
while n < 101:
    print("current number: ", n)
    n += 2
    if n == 50:
        break






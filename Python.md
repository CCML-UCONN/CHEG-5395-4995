---
layout: page
mathjax: false
permalink: /Python/
---

# Getting Started
1. [Logging Into the Computing Clusters](../Clusters/)
2. [Basic UNIX](../UNIX/)
3. [Python](../Python/)

____

## Python Tutorial

## Contents
1. [Introduction](#introduction)
2. [Running scripts](#running-scripts)
3. [Numbers and strings](#numbers-and-strings)
4. [Operators](#operators)
4. [Scope](#scope)
5. [Loops](#loops)
6. [Lists](#lists)
7. [Dictionaries](#dictionaries)
8. [File I/O](#file-io)
9. [Functions](#functions)
10. [Modules](#modules)
11. [ASE](#ase)

<a name='introduction'></a>

## Introduction
The Atomic Simulation Environment (ASE) is accessed through Python scripts, so it is thus necessary to learn some basic Python in order to perform calculations. The advantage is that ASE modules can be seamlessly used along with regular Python code, which makes it extremely easy to write scripts and programs for efficiently setting up and running a large number of calculations. Refer to the [Python documentation](https://docs.python.org/2/) for more detailed information. The following tutorial only convers the basic Python knowledge necessary for writing simple scripts.

<a name='running-scirpts'></a>

## Running scripts
Python can be run in different ways. In the terminal, run `python` to access the interactive prompt. Each line of code in a Python script can be executed interactively using the prompt. You can type `exit()` or press `ctrl + D` to exit the prompt.

```python
>>> print "Hello world!"
>>> exit()
```

The interactive prompt is useful for testing small pieces of code, but it quickly becomes impractical for non-trivial tasks.  More typically, you will be writing all your code in a `.py` file and then using the `python` command to execute the script
```bash
python scriptname.py arg1 arg2 
```

this will use the `python` command to execute `scriptname.py`, taking in arguments `arg1`, `arg2`, and etc. You can also execute a script and then run additional commands interactively using the `-i` flag.

```bash
python -i scriptname.py arg1 arg2 
```

This will execute `scriptname.py` taking in arguments `arg1` and `arg2`, and then open the interactive prompt. You can access all variables, modules, and etc. that are available in `scriptname.py`.

<a name='numbers-and-strings'></a>

## Numbers and strings

Here are some basic data types for numbers:

```python
i = 1     # an integer
i = 3/2   # −−>1, also an integer 
i = 3./2  # −−>1.5
i = 3/2.  # −−>1.5
i = 2**0.5      #−−>sqrt(2)
i = 5.1 + 2.4j  # a complex number
```
Convenient built-in functions exist for converting amongst the data types:

```python
i = int(1.)   # an integer
i = float(1)  # a floating point number
```

Strings must be terminated with the same type of quotation, either `'` or `"`. 

```python
a = 'a "string"'              # using single quotations
b = "and another 'string'"    # using double quotations
```
They can be concatenated by using the `+` operator

```python
c = a + b 
```

You can also convert numbers into strings using `str()`

```python
string = str(c)
```

You can also convert strings into numbers, as long as the content of the strings are convertible

```python
number = int('10')    # an integer
number = float('10')  # a floating point
```

Strings are containers whose elements can be accessed by their index using square brackets `[ ]` 

```python
print b[1:3]  # prints 'nd'
print len(b)  # --> 18
print ' square root of 2=%.8f ' % (0.5**0.5) # prints 8 first digits of 1/sqrt(2)
```
<a name='operators'></a>

## Operators

Here are some of the common operators for assigning and comparing values. The mathematical operators `+`, `-`, `*`, `/` are used for addition, subtraction, multiplication, and division. For exponents, the double asterick `**` is used.

The `%` operator is used to determine the remainder, as in
```python
4%3   # --> 1
```

As you have already seen, `=` is the assignment operator, as in
```python
a = 1
```

A few other convenient assignment operators are `+=`, `-=`, `*=`, `/=`, `%=`, and `**=`, which perform the operation before the equals sign before assigning it to the variable. Some examples

```python
c += a  # c = c+a
c -= a  # c = c-a
c *= a  # c = c*a
c /= a  # c = c/a
c **= a # c = c**a
```

The usual comparison operators `==`, `!=`, `>`, `<`, `>=`, and `<=` are used for testing for equallity, inequality, greater than, less than, greater or equal than, and less than or equal than. These operators return `True` or `False`.

The logical operators `and`, `or`, and `not` are convenient for using compound comparisons

```python
1 == 1 and not 1 == 2   # returns True
```

The membership operator `in` are convenient for testing if an element is inside a container.

```python
1 in [1,2,3]       # True
1 not in [1,2,3]   # False
```
<a name='scope'></a>

## Scope

In Python, scope is defined by indentation. Either tabbed spaces or regular spaces will work. As long as you are consistent, it will avoid confusing error messages. Scope is used to define code blocks in control flow (`if`, `else`, `elif`, etc.), in loops (`for` loops and `while` loops), in function definitions, and in class definitions.

```python
if a>b:
  print 'a is greater than b'
  if a>=c and a<=d:
    print '...and a lies in [c,d]'
elif a==b:
  print 'a equals b'
else :
  print 'a is less than b'
```
<a name='loops'></a>

## Loops

For loops are written using the `for <element> in <list>:` syntax, where the `<element>` represents each element in the `<list>`.

```python
for i in range(3):
  print i /2.

#output:
#    0.0
#    0.5
#    1.0
```

While loops:

```python
i = 10.
while i <1000.:
  print i
  i *= 10.5

#output:
#    10.0
#    105.0
```
<a name='lists'></a>

## Lists

Lists in Python can contain mixed data types. This sets up an empty list `a`

```python
a = []
```

The `append()` method can be used to add items into the list. It is accessed using the "dot notation," such as in `a.append()` since the `append()` is a method of the list object.

```python
a.append(1)     # list now contains integer 1
a.append('cat') # list now contains string 'cat'
```

You can print lists and their contents

```python
print b           # prints the entire list
print b[0], b[−1] # prints first and last element of b
print b[1:4]      # 2nd,3rd,4th element of b
```

Many methods are available for modifying lists

```python
c = [3,1,2]
c.sort()      #−> 1,2,3 
c.reverse()   #−> 3,2,1
c.pop(1)      #−> 3,1
print len(c)  #−> 2
```

You can also have lists of lists

```python
d = [[1.,0.,3.], [0. ,4. ,0.] , [0. ,0. ,8.]]
print d[0][2] # prints 3.0
```

Python supports a concept called list comprehension where you can generate lists concisely instead of using loops. To create a list of squares

```python
squares = []
for x in range(10):
  squares.append(x**2)
```

This can instead be done in a single line using

```python
squares = [x**2 for x in range(10)]
```

Here `range(10)` generates a list from 0 up to but not including 10 at intervals of 1, `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`.

<a name='tuples'></a>

## Tuples

Tuples are similar to lists except they are initialized using round brackets `( )` and they are immutable, which means their contents cannot be modified. These are useful if the container contains values that don't need to be modified.

```python
b = (1,2)
```

If you try `b[0] = 2` you will get `TypeError: 'tuple' object does not support item assignment`.

<a name='dictionaries'></a>

## Dictionaries

Dictionaries are one of the most convenient containers in Python. To set up an empty dictionary

```python
c = {}  # an empty dictionary
```

Dictionaries contain key-value pairs, where given key in the dictionary will return the corresponding value `dict[key] = value`. They can contain mixed data types (e.g. strings and integers at the same time). To add key-value pairs

```python
c['fish'] = 'green'
c[4] = 'blue'
c['x'] = 1
```
You can retrieve all keys and all values, or just the value corresponding to the given key

```python
print c.keys()    #−−> ['x',4,'fish']
print c.values()  #−−> [1,'blue','green']
print c[4]        #−−> 'blue'
```

You can also initialize the dictionary with all key-value pairs

```python
d = {'a':1, 'b':2, 'c':'d'}
print d['b']  #−−> 2
d['b'] = 4
print d['b']  #−−> 4
```

Dictionaries also include other convenient methods, such as `items()`, which returns a list of tuples containing the key-value pairs, and `has_key()` which returns either `True` or `False` depending on whether or not the dictionary contains the key.

```python
print d.items()      #−−> [('a', 1), ('c', 'd'), ('b', 4)]
print d.has_key('e') #−−> False
```
<a name='file-i-o'></a>

## File I/O

File input and output is important for reading in results and writing out results for the ASE calculations.

To open a file for reading or writing:

```python
f = open('file1.txt', 'r')  #open a file for reading 'r'
g = open('output.txt', 'w') #open a file for writing 'w'
for x in f.readlines():
  y = x.split() #split up each line by white spaces
  print >>g, float(y[0])/3., float(y[−1])/2.
  #write third of first and half of last column
￼￼g.close()
  f.close()
```
If the file doesn't exist, it will be created.

To open a file and add a line

```python
f = open('file1.txt', 'a') #open file in append 'a' mode
for i in range(10):
  print >> f, i
f.close()
```
To process a file line by line:

```python
f = open('biginput.txt').readlines()
for line in f:
  line.split()[0]   # split the lines by spaces and return the first element
f.close()
```

<a name='functions'></a>

## Functions

Functions are defined using `def` and the proper scope indentation. To write an addition function,

```python
def add(a,b):
  return a + 2*b
```
Then `add(1,2)` will return `5`.

<a name='modules'></a>

## Modules

A lot of useful modules are installed system-wide. They provide useful extended functionality. In addition to the `ase` modules, you will probably be using the `numpy` module most frequently. `numpy` provides `array` containers for matrix and matrix manipulation, similar to MATLAB.

To use a module, run

```python
import numpy as np
```
this imports the `numpy` module as `np`, which is just a shorthand. All methods and classes contained in the `numpy` moduled can then be accessed using the dot notation

```python
a = np.array([[1.,2.],[3.,4.]])   #initialize an array
b = np.array([[2.,4.],[6.,8.]])   #initialize another array
c = np.dot(a,b)                   #dot product
d = a + b                         #sum
```

If you only need certain methods in the module, you can import them selectively using `from`. Then the methods can be used without the module name and the dot notation.

```python
from numpy import array
a = array([[1.,2.],[3.,4.]])
```

Modules that are not loaded by default must be loaded using the `import` statement.

<a name='ase'></a>

## ASE

The Atomic Simulation Environment (ASE) is simply another Python module that can be loaded using

```python
import ase
```

Continue onto the [ASE Tutorials](../ASE) to learn more.

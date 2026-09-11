Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sort()
a=["vja","hyd","vzg","chennai"]
a.sort()
a
['chennai', 'hyd', 'vja', 'vzg']
b=[8,5,0,1,4,20,20,9]
b.sort()
b
[0, 1, 4, 5, 8, 9, 20, 20]
c=[6,9.0,"python",3+8j,True,False]
c.sort()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
a=[True,False]
a.sort()
a
[False, True]
a=["mango","berry","dragon"]
a.reverse()
a
['dragon', 'berry', 'mango']

#len()
a=["c","c++","java"]
>>> len(a)
3
>>> b="java"
>>> n
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> a.count("c")
1
>>> #clear()
>>> a=["python",".net","hadoop"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("pooja")
>>> b
['pooja']
>>> a.append()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
>>> a.append[]
SyntaxError: invalid syntax

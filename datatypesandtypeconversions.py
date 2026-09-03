Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=7
type(a)
<class 'int'>
b=5.7
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="course"
type(d)
<class 'str'>
e='''codegnan'''
type(e)
<class 'str'>
f=6+9j
type(f)
<class 'complex'>
g=6j+4
type(g)
<class 'complex'>
h=6j
type(h)
<class 'complex'>
x=5+9i
SyntaxError: invalid decimal literal
j=True
type(j)
<class 'bool'>
h=False
type(h)
<class 'bool'>
#datatypes conversions
#int
int(8)
8
int(6.7)
6
int("hi")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(6)
6.0
float(6.5)
6.5
float("hello")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
float(6+7j)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float(6+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str
str(5)
'5'
st(5.6)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    st(5.6)
NameError: name 'st' is not defined. Did you mean: 'set'?
str(5.6)
'5.6'
>>> str("hello")
'hello'
>>> str(6+7j)
'(6+7j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(5)
(5+0j)
>>> complex(6+5j)
(6+5j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(6.5)
(6.5+0j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(5)
True
>>> bool(5.5)
True
>>> bool("hi")
True
>>> bool(5+7j)
True
>>> bool(True)
True
>>> bool(False)
False

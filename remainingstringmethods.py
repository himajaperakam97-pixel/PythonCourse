Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
b.replace("java","c")
'python c'
#upper
#upper
#upper()
a="python"
a.upper()
'PYTHON'
#lower()
b="CODE"
b.lower()
'code'
c="java"
c.capitalize()
'Java'
d="i am in class"
d.title()
'I Am In Class'
e="python course"
e.title()
'Python Course'
#to write initial letter as capital we use capitalize()method
#uppercase and lowercase conditional methods
a="hello world"
a.startswith("h")
True
a.endswith("d")
True
a.isalpha()
False
b="helloworld"
b.isalpha()
True
a.isdigit()
False
b="java"
b.isalnum()
True
c="himaja123"
c.isalnum()
True
#strip()
#lstrip(),rstrip()
a="      himaja       "
a.strip()
'himaja'
a.lstrip()
'himaja       '
a.rstrip()
'      himaja'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
#example
fname="himaja"
lname="perakam"
print(fname+lname)
himajaperakam
print(fname+" "+lname)
himaja perakam
print(fname.title()+" "+lname.title())
Himaja Perakam
print((fname+" "+lname).title())
Himaja Perakam
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']
#join()
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
" ".join(b)
'vja hyd vzg'
"k".join(b)
'vjakhydkvzg'
c="hello"
"m".join(c)
'hmemlmlmo'
#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
print("the sum is,a+b")
the sum is,a+b
city="vja"
print("city is",city)
city is vja
#2nd method format()
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello{}".format(a,b))
hello motu hellopatlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
#fstring()
a="virat"
b="kohli"
print(f"hello {a}{b}")
hello viratkohli
print(f"hello {a} {b}")
hello virat kohli
print(f"hello {a} hello {b}")
hello virat hello kohli
fname="himaja"
lname="sai"
>>> print("{} {}" .format(fname,lname))
himaja sai
>>> print(f"{fname} {lname}")
himaja sai
>>> 
>>> 
>>> a=2
>>> b=5
>>> c=a+b
>>> print("the sum is {}".format(c))
the sum is 7
>>> print(f"the sum is {c}")
the sum is 7
>>> print(f"the sum is {a+b}")
the sum is 7
>>> print("the sum is {a+b}".format(a+b))
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print("the sum is {a+b}".format(a+b))
KeyError: 'a+b'
>>> print("the sum is {}".format(a+b))
the sum is 7
>>> print("the sum is {}".format(a+b))
the sum is 7
>>> a=10
>>> b=20
>>> swap(b)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    swap(b)
NameError: name 'swap' is not defined

Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=["code","codegnan","python"]
>>> a.upper()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> b=str(a)
>>> b.upper
<built-in method upper of str object at 0x000001F619709930>
>>> b.upper()
"['CODE', 'CODEGNAN', 'PYTHON']"
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> b=set(a)
>>> b
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> b.reverse()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b.reverse()
AttributeError: 'set' object has no attribute 'reverse'
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.split()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.split()
AttributeError: 'list' object has no attribute 'split'
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
a2=a[5:10]
a2
[4, 6, 3, 7, 0]
a1.sort()
a1
[1, 2, 5, 8, 9]
a2.sort()
a2
[0, 3, 4, 6, 7]
a1.reverse()
a1
[9, 8, 5, 2, 1]
a2.reverse()
a2
[7, 6, 4, 3, 0]
c=a2+a1
c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]

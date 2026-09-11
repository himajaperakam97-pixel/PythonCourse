Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(5,7.8,"himaja",4+9j,True,False)
>>> print(a)
(5, 7.8, 'himaja', (4+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.count(4+9j)
1
>>> a.index(False)
5

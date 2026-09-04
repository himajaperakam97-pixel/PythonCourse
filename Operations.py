Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arithmetic
>>> a=2
>>> b=4
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a//b)
0
>>> print(a/b)
0.5
>>> print(a%b)
2
>>> print(a**b)
16
>>> #assignment
>>> a=3
>>> b=6
>>> a+=b
>>> a
9
>>> a-=b
>>> a
3
>>> a*=3
>>> a
9
>>> a//4
2
>>> a//=4
>>> a
2
>>> a%=2
>>> a
0
a**=4
a
0
a
0
b
6
#updation for b
a=3
b=6
b+=a
b
9
b-=2
b
7
b*=3
b
21
b//4
5
b/5
4.2
b%2
1
b**4
194481
b
21
#comparision
a=8
b=10
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
a<=b
True
b>=a
True
a>=b
False
b>=a
True
b<=a
False
#logical
a=5
b=10
a<b and b>a
True
a>b and b>a
False
a!=b and a==b
False
a<b and b>a
True
a>b or b>a
True
a<=b or b<=a
True
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
#identify
a=4
type(a) is int
True
type(a) is not int
False
b=5.6
type(b) is float
True
type(b) is not float
False
#membership
a=3,4,5,6,7,8,9
9 in a
True
10 in a
False
2 not in a
True
True
True
#bitwise
a=2
b=6
a&b
2
a|b
6
a=4
~a
-5
b=-6
~b
5
a=3
b=5
a^b
6
a=3
b=5
a^b
6
a=4
a<<2
16
a=3
a>>2
0
a=7
a>>3
0

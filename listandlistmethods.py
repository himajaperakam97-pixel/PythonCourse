Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=4.5
type(b)
<class 'float'>
c=[4.5]
type(c)
<class 'list'>
a=["python","java",<class 'list'>
   
SyntaxError: invalid syntax
#append()
   
a=["python","java","c"]
   
a.append("c++")
   
a
   
['python', 'java', 'c', 'c++']
a.append("ml","ai")
   
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
   
a
   
['python', 'java', 'c', 'c++', ['ml', 'ai']]
#extend()
   
a=["ds","ai","ml"]
   
a.extend(["c","c++"])
   
a
   
['ds', 'ai', 'ml', 'c', 'c++']
#insert()
   
a=["black","white"]
   
a.insert(1,"blue")
   
a
   
['black', 'blue', 'white']
a=["apple","banana","grapes"]
   
a.index("grapes")
   
2
#copy()
   
a.copy()
   
['apple', 'banana', 'grapes']
b=a.copy()
   
b
...    
['apple', 'banana', 'grapes']
>>> #pop()
...    
>>> a=["hi","hello","how","are","you"]
...    
>>> a.pop()
...    
'you'
>>> a
...    
['hi', 'hello', 'how', 'are']
>>> a.pop("how")
...    
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.pop("how")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(2)
...    
'how'
>>> a
...    
['hi', 'hello', 'are']
>>> #remove()
...    
>>> a.remove("hello")
...    
>>> a
...    
['hi', 'are']

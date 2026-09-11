Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
#set is an unorder collection
#set is a semi-mutable
a={7,4.5,"python",5+9j,True,False}
print(a)
{False, True, (5+9j), 4.5, 7, 'python'}
type(a)
<class 'set'>
b={7,9,4,0,1,4,7,9}
print(b)
{0, 1, 4, 7, 9}
#add()
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a={4,5,6,7,8,9}
b={7,8,9}
b.issubset(a)
True
a.issubset(b)
False
#superset()
a={6,7,8,9,10,11,12}
b={10,11,12}
a.issuperset(b)
True
b.issuperset(a)
False
#superset is the main set
#subset is the another part of a main set
#union()-merging of two sets
a={3,4,5,6,7}
b={5,6,7,8,9,10}
a.union(b)
{3, 4, 5, 6, 7, 8, 9, 10}
#intersection()- collects the common elements
a={10,11,12,13,14,15}
b={14,15,16,17}
a.intersection(b)
{14, 15}
#update()
a={2,3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
#difference()
a={6,7,8,9,10,11}
b={2,3,4,5,6,7,8}
a.difference(b)
{9, 10, 11}
b.difference(a)
{2, 3, 4, 5}
#symmetric_difference()-deletes the same values in a given set
a={7,8,9,10,11,12,13}
b={10,11,12,13,14,15}
a.symmetric_difference(b)
{7, 8, 9, 14, 15}
#difference_update()
a={3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.difference_update(b)
a
{3}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9, 10}
{4, 5, 6, 7, 8, 9, 10}
{4, 5, 6, 7, 8, 9, 10}
#intersection_update()
a={3,4,5,6,7,8}
b={1,3,6,7,8,9,10}
a.intersection_update(b)
a
{8, 3, 6, 7}
b.intersection_update(a)
b
{8, 3, 6, 7}
#symmetric_difference_update()
a={6,7,8,9,10,11,12}
b={10,11,12,12,14,15}
a.symmetric_difference_update(b)
a
{6, 7, 8, 9, 14, 15}
b.symmetric_difference_update(a)
b
{6, 7, 8, 9, 10, 11, 12}
#pop()-pick any element and deletes it
a={10,20,30,40,50}
a={10,20,30,40,50}
a.pop()
50
a
{20, 40, 10, 30}
a.pop()
20
#remove - removes the specific elements
a.remove(20)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.remove(20)
KeyError: 20
a.remove(10)
a
{40, 30}
#discard()
f={4,5,6,7,8,9}
f.discard(8)
a
{40, 30}
f
{4, 5, 6, 7, 9}
#copy()
f.copy()
{4, 5, 6, 7, 9}
g=f.copy()
g
{4, 5, 6, 7, 9}
#clear()
a={3,4,5,6,7}
a.clear()
a
set()
>>> #add()
>>> b.add(50)
>>> b
{6, 7, 8, 9, 10, 11, 12, 50}
>>> j={5,6,7,8}
>>> len(j)
4
>>> h.index(4)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    h.index(4)
NameError: name 'h' is not defined
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> k={3,4,5,6,7,8}
>>> l={2,3,4,6,7}
>>> k.isdisjoint(l)
False
>>> m={6,7,8,9}
>>> n={1,2,,3,4}
SyntaxError: invalid syntax
>>> n={1,2,3,4}
>>> m.disjoint(n)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    m.disjoint(n)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?

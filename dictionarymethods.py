Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #pop()
>>> a={"week":"wed","date":9}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("week")
'wed'
>>> a
{'date': 9}
>>> #popitem()
>>> a={"country":"india","state":"ap"}
>>> a.popitem()
('state', 'ap')
>>> a
{'country': 'india'}
>>> #copy()
>>> a={"name":"pooja","course":"python","duration":100}
>>> a.copy()
{'name': 'pooja', 'course': 'python', 'duration': 100}
>>> len(a)
3
>>> #clear()
>>> a.clear()
>>> a
{}
>>> a={"name":"pooja","year":2026,"name":"pooja"}
>>> print(a)
{'name': 'pooja', 'year': 2026}
a={"name":"pooja","year":2026,"name":"priya"}
print(a)
{'name': 'priya', 'year': 2026}
a={"name":"pooja","year":2026,"name1":"pooja:}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"name":"pooja","year":2026,"name1":"pooja"}
   
print(a)
   
{'name': 'pooja', 'year': 2026, 'name1': 'pooja'}
#giving multiple keys in dictionary
   
a={"idnos":[10,20,30],"names":["pooja","priya","sathvika"],"places":["vja","hyd","vzg"]}
   
print(a)
   
{'idnos': [10, 20, 30], 'names': ['pooja', 'priya', 'sathvika'], 'places': ['vja', 'hyd', 'vzg']}
type(a)
   
<class 'dict'>
a.keys()
   
dict_keys(['idnos', 'names', 'places'])
a.values()
   
dict_values([[10, 20, 30], ['pooja', 'priya', 'sathvika'], ['vja', 'hyd', 'vzg']])
a.items()
   
dict_items([('idnos', [10, 20, 30]), ('names', ['pooja', 'priya', 'sathvika']), ('places', ['vja', 'hyd', 'vzg'])])

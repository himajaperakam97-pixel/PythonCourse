Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
b="work until you succeed"
b[5:10]
'until'
b[14:21]
' succee'
b[14:22]
' succeed'
b[11:15]
'you '
b[11:14]
'you'
b[0:4]
'work'
c="vijayawada is a royal city"
c[22:25]
'cit'
c[22:26]
'city'
c[16:21]
'royal'
c[0:10]
'vijayawada'
c[11:13]
'is'
d="Happy Teachers day"
d[-18:-14]
'Happ'
d[-18:-15]
'Hap'
d[-18:-13]
'Happy'
d[-3:0]
''
d[-3:-1]
'da'
d[-3:-2]
'd'
d[-3:-3]
''
d[-3:-4]
''
d[-3:]
'day'
d[-12:-6]
'Teache'
d[-12:-5]
'Teacher'
h="vizag is a city of destiny"
h[-26:-21]
'vizag'
h[-15:-11]
'city'
h[-7:-1]
'destin'
h[-7:]
'destiny'
#striding
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
\
                                                                                                                                                           'dt cec'
SyntaxError: unexpected indent

c="cloud computing"
c[1:7:2]
'lu '
c[2:13:3]
'o mt'
c[4:14:5]
'dp'
c[3:12:6]
'up'
>>> b="Machine learning"
>>> b[::3]
'Mheeng'
>>> b[::5]
'Mnag'
>>> b[::2]
'Mcielann'
>>> b[::9]
'Me'
>>> b[:7]
'Machine'
>>> b[3:11]
'hine lea'
>>> b[5:]
'ne learning'
>>> #negative striding
>>> #negative striding
>>> a="python course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-5]
'uo'
>>> a[-6:-12:-2]
'cnh'
>>> a[7:3:2]
''
>>> #highest to lowest value is given then we will get empty string
>>> a[-9:-5:-2]
''
>>> #lowest to highest value is given then we get empty string
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'

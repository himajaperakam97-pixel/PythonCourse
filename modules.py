'''def greetings(name):
    print("welcome",name)'''

'''a=10
b=20
print("sum is",a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a*b)'''

details={"idnos":[10,20,30],"names":["himaja","sai","pavan"],
         "marks":[70,80,90]}

'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''        


#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(4))
print(math.pow(2,4))
print(math.log(10))
print(math.cos(45))
print(math.tan(60))
print(math.ceil(3.9))
print(math.ceil(9.12))
print(math.floor(6.9))'''

#by using from variable we can import variables

'''from math import pi,log,sqrt,tan
print(pi,log(2),sqrt(9),tan(45))'''

#sys module
'''import sys
print(sys.path)'''

'''for i in sys.path:
    print(i)'''

#print(sys.version)

#os module
#a software which interacts with the computer
#cwd-current working directory
#import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("oct5"))
#print(os.listdir())
#print(os.chdir("C:\\Users\\USER\\Downloads"))
#print(os.listdir())

#random module
#sample
'''import random
a=random.sample(range(10,50),5)
print(a)'''

#randint()
'''import random
a=random.randint(5,12)
print(a)'''

#choice
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

#task
'''import random
n=int(input("roll the dice"))
m=random.randint(1,6)
option=input("enter the options:\n1.yes\n2.no")
if option=="yes":
    print(n)
else:
    print("stop")'''

#the correct version of code
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again? (y/n)")
    if option=="y":
        continue
    elif option=="n":
        break'''

#calendar module
'''import calendar
year=2026
month=10
print(calendar.month(year,month))'''

'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''

#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"rem year is {b.tm_yday}-{b.wday}")'''

#task -> generate 10 random numbers and give a time limit
'''import random
import time
for i in range(10):
    a=random.randint(1,10)
    print(a)
    time.sleep(2)'''

#regular expressions(regex)
#regular expressions are powerful tools embedded in python which is mainly used to find a patterns
#within a given string or statements or files and mainly using for text manipulation
'''a="codegnan is in vja"
print(a)

a="codegnan\nis\tin\nvja"
print(a)'''

'''a=r"codgnan\nis\tin\nvja"
print(a)'''

#there are 5 steps in regular expressions
#compile(),search(),findall(),split(),sub()

#sequence characters
'''\w->it matches alphanumeric
\W->it matches no-alphanumeric
\d->it matches any digit
\D->it matches non-digits
\s->it represents white spaces and used to remove the white spaces
\S->it represents non white spaces'''

#complie()
import re
a="code map money cash cap maths cup cat mug mat"
b=re.compile(r"m\w\w\w\w")
print(b)

'''#search()
c=b.search(a)
print(c)'''

c=re.search(r"m\w+",a)
print(c)

#findall()
'''b=re.findall(r"m\w+",a)
print(b)

b=re.findall(r"c\w+",a)
print(b)'''

#split()
'''c=re.split(r"m",a)
print(c)

d=re.split(r"\s",a)
print(d)'''

#sub()
'''e=re.sub(r"m","k",a)
print(e)'''

#task
import re
n="5,6,3.2,9, himaja,python"
j=re.findall(r"\d+",n)
print(j)

import re
n="5,6,3.2,9, himaja,python"
j=re.findall(r"\D+",n)
print(j)







































































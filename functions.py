'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the division is",a//b)
    print("the power is",a**b)
    print("the mod division is",a%b)
calculate(10,20)
calculate(2,5)
calculate(5,6)'''
'''def add(a,b):
    c=a+b
    print(c)
add(4,5)'''
'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''    

'''def fullname():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return a*b
print(mul(5,2))'''

#print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(5,4))'''

#task
'''def calculate():
    a=int(input("Enter a value"))
    b=int(input("Enter b value"))
    option=int(input("select (opt1/opt2/opt3)"))
    if(option==1):
        print(a+b)
    elif(option==2):
        print(a-b)
    else:
        print(a*b)
    calculate()
calculate()'''

#2nd method
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    option=int(input(choose the option
                         1.add
                         2.sub
                         3.mul))
    if option==1:
        add()
    elif option==2:
        sub()
    else:
        mul()'''

#splitbill()
'''def splitbill():
    a=int(input("enter the total members:"))
    b=int(input("enter the total amount:"))
    print("perhead bill is",b//a)
splitbill()'''

'''def splitbill():
    a=int(input("enter the total members:"))
    b=int(input("enter the total amount:"))
    print("perhead bill is {}".format(b//a))
splitbill()'''

'''def splitbill():
    a=int(input("enter the total members:"))
    b=int(input("enter the total amount:"))
    print(f"perhead bill is {b//a}")
splitbill()'''    
          
        
'''def splitbill():
    a=int(input("enter the total members:"))
    b=int(input("enter the total amount:"))
    c=b//a
    print("perhead bill is {}".format(c))
    print(f"perhead bill is {c}")
splitbill()'''

#keyword and positional arguments
'''def Details(id,name,mailid):#1st step
    id=10
    name="himaja"
    mailid="himaja@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")#2nd step by using positional arguments
Details(id=20,name="himaja",mailid="h@gmail.com")
Details(id=30,name="gayathri",mailid="g@gmail.com")
Details(40,"mokshitha","m@gmail.com")#without giving keywords we can enter the details
Details("vinay","v@gmail.com",50)#without giving the keywords we get the output but in inorder'''

#task
#employee->name,salary,designation
'''def Employee(name,salary,designation):
    name="himaja"
    salary=50000
    designation="Developer"
    print(name,salary,designation)
Employee(name="name",salary="salary",designation="designation")'''

'''def Employee(name,salary,designation):
    print(name,salary,designation)
Employee(name="name",salary="salary",designation="designation")
Employee(name="Himaja",salary="75000",designation="Data analyst")
Employee(name="satvika",salary="75000",designation="Developer")
Employee("SaiPavan","50000","Testing")
Employee("25000","Webdeveloper","Nandini")'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",1800)'''

'''def grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dal")'''

'''def grocery(item="ghee",price):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(500)'''

#bakery->cake,price,qty
'''def bakery(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.f" %qty)
bakery("chocolate",1200,1)'''

'''def bakery(cake="red velvet",price=2000,qty=2):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.f" %qty)
bakery()'''

'''def bakery(cake,price=500,qty=1):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.f" %qty)
bakery("black forest")'''

'''def bakery(cake="strawberry",price=200,qty=2):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.f" %qty)
bakery()'''    

#* arguments-> * is used to unpack the elements
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''b=(5,6,7,8,9)
print(b)
print(*b)'''

'''c={8,9,10,11,12}
print(c)
print(*c)'''

'''d={"name":"pooja","year":2026}
print(d)
print(*d)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''
    
'''a,b,c="codegnan"
print(a)
print(b)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
print(c)'''#error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''

#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()    
b=[4,5,6,7,8,9]
check(*b)
c=(3,4,5,6)
check(*c)
d={6,7,8,9}
check(*d)
e={"year":2026,"month":"sep"}
check(*e)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in(int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,5,3.4,4.2,5.3)
check1(3,4,5,6,3.2,4.4,"himaja")'''

#kwargs(**)-keyword arguments
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["himaja","sai","satvika"],
   "marks":[20,30,40],"status":["a","p","p"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["himaja","sai","satvika"],
   "marks":[20,30,40],"status":["a","p","p"]}
details(**d)'''

#both * and **
def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
final()
data=(2,3,4,5,3.4,5.2)
final(*data)
details={"name":["bhavika","sowmya","priya"],
         "marks":[60,70,80]}
final(**details)
final(*data,**details)
        

    





























    

























































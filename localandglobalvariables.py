#global and local variables
#first case of global variable
'''a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''
#second case of global variables
'''a=5
def check1():
    a=10
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''
#third case of both global and local variables
'''a=3
b=2
def check2():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is",b)'''
#usage of global keyword
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    #global b
    b=13
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)'''

#ASCII-American Standard code of Information Interchange
#CHR,ORD
'''print(chr(65))
print(chr(90))
print(chr(92))

print(ord("a"))
print(ord("z"))'''

#print(ord(98))-should use only string
#print(chr("a"))-should use only number

#task
#print a to z in a single line
'''for i in range(65,91):
    print(chr(i),end=" ")'''
    
'''for i in range(97,123):
    print(chr(i),end=" ")'''

'''n=input("Enter your name")
for i in n:
    print(i,ord(i))'''

#task
#Raliway Ticket
'''def ticket():
def gender():
    price=int(input("enter the amount:"))
    gender=input("enter the gender:"))
    if gender=="male":
        total_amount=(total_amount/price)*100
     else:
         print("the amount is")
    elif gender=="female":'''

'''while True:      
    def ticket_price(gender,age):
        price=1000
        if gender=="male":
            if age>60:
                discount=price*30/100
                final_price=price-discount
                category="Male Senior Citizen"
                else:
                    final_price=price
                    category="Male Normal Citizen"
            elif gender=="female":
                if age>60:
                    discount=price*50/100
                    final_price=price-discount
                    category="Female Senior Citizen"
                else:
                    final_price=price*20/100
                    final_price=price-discount
                    category="Female Normal Citizen"
                else:
                    print("Invalid gender")
                    return
                print("Gender:",gender)
                print("Age:",age)
                print("Category:",category)
                print("Ticket Price:",price)
                print("Final Price:",final_price)
    gender=input("Enter the gender(male/female):").lower()
    age=int(input("enter age:"))
    ticket_price(gender,age)'''

#the correct code is
'''while True:
    def railway_ticket():
        ticket=1000
        gender=input("enter the gender")
        age=int(input("enter the age"))
        if gender=="m":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
        elif gender=="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
    railway_ticket()'''

#generators
#a=(expr for var in collection/range)
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(a)
print(*a)
print(type(a))'''

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''
a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))    





























    
        

























































    

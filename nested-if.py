#nested-if
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a>b:
    print("less")
if b>a:
    print("greater")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("equal")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''


'''a=60
b=80
if a>b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")'''

#nested-if using logical operator
#and,or,not
'''a=20
b=40
if a<b and b>a:
    print("true")
    if b>a or a<b:
        print("false")
    elif a!=b:
        print("number exists")'''

#nested if using identify operator
#is,not is
'''a=40
b=20
if type(a) is int:
    print("true")
    if type(b) is not int:
        print("false")
else:
    print("condition satisfied")'''

#nested if using membership operator
#in,not in
'''a=[20,25,30,35,40]
if 20 in a:
    print("true")
    if 35 not in a:
        print("false")'''
        
        

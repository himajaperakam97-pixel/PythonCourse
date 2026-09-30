#generator
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
'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    #return "python"
    #return "java"
    #return "c"
    return "python","java","c"
print(*mygen())'''

'''def mygen():
    yield "hyd"
    yield "vja"
    yield "vzg"
print(*mygen())
#next()-this build-in function is used to when we want to get single output
b=mygen()
print(next(b))
print(next(b))
print(next(b))
#print(next(b))'''

#built-in functions
#max(),min(),sum(),len(),print(),input(),type(),next(),range()
a=[4,5,10,20,25,30]
print(max(a))
print(min(a))
b,c=10,20
print(sum(b,c))
d="python"
print(len(d))
print(a)
g=input("Enter your name:")
h=input("enter your age:")
print(type(g))


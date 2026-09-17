#loops
#for,while,range,break,continue,pass
#for loop()
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end="")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(6,7,8,9,10)
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={4,5,6,7,8,9,10,6,8}
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={"year":2026,"month":"sep","date":16}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[5.5,4.5,6.7]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=["python","java"]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[4+7j,7+2j]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[4,7.8,"python",3+9j,True,False]
print(type(a))
for i in a:
    print(i)
    print(type(i))'''

'''a=["apple","banana","grapes"]
b=str(a)
for i in b.upper():
    print(i,end=" ")'''

      
'''a=["apple","banana","grapes"]
result=[i.upper()for i in a]
print(result)'''
#answer for the task
a=["apple","banana","grapes"]
'''b=str(a)
print(b.upper())
for i in a:
    print(i.upper(),end=" ")'''
b=[]
for i in a:
    b.append(i.upper())
print(b)    


      
    

#list comprehension
'''a=["python","java","dsa"]'''
#["PYTHON","JAVA","DSA"]
#print(a.upper())
'''for i in a:
    print(i.upper(),end=" ")'''
'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#syntax
#a=[expression for var in collection/range]
#
'''b=[i.upper() for i in a]
print(b)'''

'''#task
b=["apple","mango"]
#["Apple","Mango"]
c=[i.title() for i in b]
print(c)'''

'''a=[1,2,3,4,5,6,8,12,13]
#a=[1,4,9,25,36,64,144,169]
b=[i**2 for i in a]
b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)'''

'''c=[i for i in range(21)]
print(c)'''

'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i*i for i in range(31) if i%2==0]
print(a)'''

a=["grapes","berry","mango","kiwi","dragon","apple"]
'''b=[i.find("a") for i in a]
print(b)'''
'''b=[i for i in a if "a" in i]'''
'''b=[i for i in a if "a" not in i]
print(b)'''

#no-elif usage in list comprehension

#if-else usage in list comprehension
'''a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
'''c=[i+i for i in range(1,6) for i in range(1,6)]
print(c)'''
'''c=[a[i]+b[i] for i in range(5)]'''
c=[a[i]+b[i] for i in range(len(a))]
print(c)

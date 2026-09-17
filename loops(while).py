#whileloop
#while loop is continuous iteration
'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=20
while a>=1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    a=a-1
    print(a)'''

'''a=20
while a>1:
    a=a-1
print(a)'''

'''a=30
while a>1:
    print(a)
    a+=1'''
#when the value is high we shouldnot use increment operator
'''a=30
while a>1:
    print(a)
    a-=1'''
#here the value is high so we used decrement operator
'''a=5
while a<15:
    print(a)
    a+=1'''

#voting
'''while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")'''
#here while True condition must be used the run time inputs at the beginning of the code


#range()-is a sequential iteration
#start-stop-step
'''for i in range(10):
    print(i)'''
'''for i in range(15,30):
    print(i)'''
'''for i in range(0,20,2):
    print(i,end=",")'''

'''for i in range(5,50,5):
    print(i,end=",")'''

'''for i in range(3,30,3):
    print(i,end=",")'''

#task
#student marks
'''marks=int(input("enter marks:"))
while marks>0:
    for i in range(91,101):
        print("Grade-A")
    for i in range(81,91):
        print("Grade-B")
    for i in range(71,81):
        print("Grade-C")
    for i in range(50-71):
        print("Grade-D")
    for i in range(51):
        print("Fail")'''

#the correct version of the code is
'''while True:
    marks=int(input("enter the marks"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail,Study well......")'''

#attendence tracker
while True:
   n=int(input())
   p=0
   ab=0
   for i in range(n):
       c=input()
       
       

    

        
        




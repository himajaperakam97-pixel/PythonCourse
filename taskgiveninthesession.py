#max(),min(),sum()
'''print(max(2,4,5,7,8,10,20))
print(min(2,4,5,7,8,10,20))
#print(sum(10,20))
a=3,4,5,6,7,8,9
print(sum(a))

print(sum([3,4,5,6,7,8]))'''


'''a=int(input("Enter no of students:"))
students=[90,70,40,20,60]
avg=students/5
print("......Marks Analysis Report.....")
print("Heightest marks:",max(90,70,40,20,60))
print("lowest marks:",min(90,70,40,20,60))
print("Total marks:",sum(students))
print("Average:",avg)'''

#the correct code is
'''student_count=int(input("Enter no of students:"))
a=[]
for i in range(1,student_count+1):
    marks=int(input(f" student no. {i} marks"))
    a.append(marks)
print("Total students:", student_count)
print("Highest marks:", max(a))
print("Lowest marks:", min(a))
print("Total marks:", sum(a))
print("Average marks:", sum(a)/student_count)'''


#BMI
'''while True:
    weight=float(input("Enter your weight:"))
    height=float(input("Enter your height:"))
    bmi=weight/(height)**2
    if bmi<18.5:
        print("Underweight")
    elif bmi>18.5 and bmi<=24.5:
        print("Healthy weight")
    elif bmi>24.5 and bmi<=29.5:
        print("over weight")
    else:
        print("obesity")'''

#patterns
#right angled triangle
'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()'''
#reversed right angled triangle
'''n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()'''
'''#2nd method in reversed right angled triangle
n=int(input())
for i in range(n,0,-1):
    print("*"*i)'''
#square
'''n=int(input())
for i in range(1,n+1):
    for j in range(n):
        print("*", end=" ")
    print()'''
#pyramid
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*",end=" ")
    print()'''

n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="") 
    for j in range(i):
        print("*",end=" ")
    print()    




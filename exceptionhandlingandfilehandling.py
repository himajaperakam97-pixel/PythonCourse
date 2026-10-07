#exception handling
#there are 3 main types of exception handling
#try,except,else,finally
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends")'''
'''a=int(input("a value"))
b=int(input("b value"))
try:
    c=a//b
    print(c)
except:
    print("exception is raised")
else:
    print("no exception")
finally:
    print("programs ends")'''


#file handling
#write()-
'''a=open("himaja.txt","w")
a.write("python full stack")
a.close()'''

'''a=open("himaja.txt","w")
a.write("vijayawada")
a.close()'''

#append()
'''a=open("himaja.txt","a")
a.write("\thyd")
a.close()'''

#task
#give a data in runtime and store in the file
'''a=open("himaja.txt","w")
a.write(input("data"))
a.close()'''

#2nd method
'''a=open("himaja.txt","w")
b=input("data")
a.write(b)
a.close()'''

#read()and readline()
#a=open("himaja.txt")
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#it will display entire data and with \n
#print(a.read(10))#it will display no.of characters

#writelines()->it makes every object side by side
'''a=open("python.txt","w")
b=["priya","sowmya","himaja","bhavika","uma"]
a.writelines("\n".join(b))
a.close()'''

#file accessing
'''a=open("runtime.py")
print(a.read())'''

'''a=open("C:\\Users\\USER\\Downloads\\pythonCG\\modules.py")
print(a.read())'''



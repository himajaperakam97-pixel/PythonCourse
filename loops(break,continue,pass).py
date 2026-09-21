#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==4:
        break
    print(a)'''

'''for i in range(10):
    if i==8:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print(a)'''#error
#break can't work without loops
'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    a=a-1
    if a==12:
        continue
    print(a)'''

'''for i in range(15):
    if i==10:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#pass
'''a=5
while a>1:
    print(a)
    a=a-1
    if a==2:
        pass'''

'''for i in range(25):
    if i==10:
        pass
    print(i)'''

#ATM Application
'''balance=100000
card="c"
pwd=1234
card1=input("Enter Type of Card:")
if card==card1:
    print("Welcome Himaja")
    pwsd=int(input("Enter the Password:"))
    if pwd==pwsd:
        option=int(input("Options:\n1.Balance Enquiry \n2.Withdrawal\nEnter Option:"))
        if option==1:
            print(f"Your Balance: {balance}")
            elif option==2:
                withdraw=int(input("enter Amount:"))'''
                

#The correct version of this code
while True:
    account=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("Welcome Himaja")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option
                               1.Balance Enquiry
                               2.withdraw'''))
            if option==1:
                print("your acc bal is",account)
            elif option==2:
                money=int(input("enter the amount"))
                print(money)
                balance=account-money
                print("remaining acc balance is",balance)
            else:
                print("invalid option")
        else:
            print("Incorrect password")
    else:
        print("invalid card")
        

    

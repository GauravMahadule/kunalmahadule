# Write a Program to demonstrate Banking System.
print("*********Welcome to SBI ATM***********")
print("")
print("Please enter your PIN")
PIN = int(input())

if PIN==1234:
    
 for i in range(0,3):
    
    print("*********Welcome to SBI ATM***********")
    print("")
    print("Hi... Karan")
    print("If You want to Check Account Balance press 1")
    print("If You want to Withdraw Cash from your Account press 2")
    print("If You want to Diposite Cash press 3")

    z = int(input())
    amount = 10000
    
    if z==1: 
        print("Your Account Balance is ", amount)
    
    if z==2:
        print("Enter the Amount you want to withdraw")
        a = int(input())
        balance = amount - a
        print("Your Current Balance is ", balance)
   
    if z==3:
        print("Enter the Amount you want to Deposite") 
        b = int(input())
        currentBalance = balance+b
        print("Your Current Balance is ", currentBalance)
       

if PIN==9823:
    
 for i in range(0,3):
    
    print("*********Welcome to SBI ATM***********")
    print("")
    print("Hi... Rohan")
    print("If You want to Check Account Balance press 1")
    print("If You want to Withdraw Cash from your Account press 2")
    print("If You want to Diposite Cash press 3")

    z = int(input())
    amount = 50000

    if z==1: 
        print("Your Account Balance is ", amount)
    
    if z==2:
        print("Enter the Amount you want to withdraw")
        a = int(input())
        balance = amount - a
        print("Your Current Balance is ", balance)
   
    if z==3:
        print("Enter the Amount you want to Deposite") 
        b = int(input())
        currentBalance = balance+b
        print("Your Current Balance is ", currentBalance)
           
 
print("Thanks for Using SBI ATM")




















































































# amount = 10000;
# print("Your Account Balance is:-" , amount)

# print("Enter the amount you want to deposite")
# a = int(input())

# amount = int(amount) + int(a)
# print("Your account balance is " , amount)

# print("Enter the amount you want to Withdraw")
# b = int(input())

# amount = int(amount) - int(b)
# print("Your account balance is " , amount)



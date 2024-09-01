print("Welcome to 🪙🪙🪙🪙🪙🪙INDIAN BANK🪙🪙🪙🪙🪙🪙")


AccountNo = ""
CusName = ""
Bcode = ""
mobile = 0
balance = 50000  
def open_account():
    name=input("Enter your name:")
    AadharNo=input("Enter your Aadhar Number:")
    pancardno=input("Enter your Pan card number:")
    mobile=input("Enter your mobile number")
    print("Thank you for opening an account in our bank")

def creditamount():
    global AccountNo, CusName, Bcode, mobile
    AccountNo = input("Enter your Account Number: ")
    CusName = input("Enter your name: ")
    Bcode = input("Enter your Branch code: ")
    mobile = int(input("Enter your mobile number: "))
    print("Amount credited succesfully!!!")

def showAccountdetails():
    print("Account No:", AccountNo)
    print("Customer name:", CusName)
    print("Branch code:", Bcode)
    print("Your mobile number:", mobile)

def Deposit(amount):
    global balance
    balance += amount
    checkbalance()

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        checkbalance()

def checkbalance():
    print("Current balance:", balance)

print("1. Create account💸💸💸")
print("2.credit🤑🤑🤑")
print("3. Withdraw💲💲💲")
print("4. Deposit💰💰💰")
print("5. Check balance💶💶💶")

ch = int(input("Select any option: "))
if ch == 1:
    open_account()
elif ch == 2:
    creditamount()
elif ch == 3:
    amount = int(input("Enter amount to withdraw: "))
    withdraw(amount)
elif ch == 4:
    amount = int(input("Enter amount to deposit: "))
    Deposit(amount)
elif ch == 5:
    checkbalance()
else:
    print("Please select a valid option.")

user_exit = input("Would you like to exit? (yes/no): ")
if user_exit.lower() == "yes":
    print("Thank you for using INDIAN BANK!")
else:
    print("Thank you for visiting.")

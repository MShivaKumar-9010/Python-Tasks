
def deposit(balance):
    amount=int(input("enter your amount:"))
    balance+=amount
    print("amount deposited sucessfully!")
    print("availble balance: ",balance)
    return balance
def withdrawl(balance):
    withdrawl_amount=int(input("emter your amount:"))
    balance-=withdrawl_amount
    print("transaction successful")
    print("availble balance: ",balance)
    return balance
def check_balance(balance):
    print("available_amount:",balance)
def menu():
    balance=5000
    print("===welcome to icici Bank===")
    while True:
        print("1.deposit")
        print("2.withdrawl")
        print("3.check_balance")
        print("4.Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            balance=deposit(balance)
        elif choice==2:
            balance=withdrawl(balance)
        elif choice==3:
            check_balance(balance)
        elif choice==4:
            print("Thank for visiting our bank!")
        else:
            print("invalid choice")
menu()
































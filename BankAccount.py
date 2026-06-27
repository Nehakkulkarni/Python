class BankAccount:
    def __init__(self, account_number, name, balance = 0):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")
    def display(self):
        print("Account Details: ")
        print("Account No: ",self.__account_number)
        print("Owner Name: ",self.__name)
        print("Balance: ",self.__balance)

acc1 = BankAccount(101,"Riddhi",56400)
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.withdraw(5000)
acc1.display()
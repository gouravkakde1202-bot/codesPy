# Use encapsulation to protect and validate data within a class
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  
        self.__balance = initial_balance        

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

my_account = BankAccount("123456789", 1000)
my_account.deposit(500)
my_account.withdraw(200)
print(f"Account Number: {my_account.get_account_number()}")
print(f"Current Balance: {my_account.get_balance()}")

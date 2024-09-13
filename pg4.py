class BankAccount:
    def __init__(self, accountname, accountno, balance=0):
        self._accountno = accountno
        self._accountname = accountname
        self.__balance = balance  # Use double underscore for private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_name, balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)


account = BankAccount("12345", "Pawan", 1000)
account.deposit(1000)
account.withdraw(500)

vector1 = Vector(2, 3)
vector2 = Vector(4, 5)
print("Vector sum:", vector1 + vector2)

savings_account = SavingsAccount("67890", "Chan", 1000)
savings_account.add_interest()
print("Savings account balance:", savings_account.get_balance())

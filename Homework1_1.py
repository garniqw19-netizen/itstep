class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Баланс поповнено на {amount} грн")
        print(f"Новий баланс: {self.balance} грн")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount} грн")
            print(f"Новий баланс: {self.balance} грн")
        else:
            print("Недостатньо коштів на рахунку")


account = BankAccount("202020", 10000)

choice = input("Що ви хочете зробити (зняти/поповнити): ")

if choice == "зняти":
    amount = int(input("Яку суму ви хочете зняти: "))
    account.withdraw(amount)

elif choice == "поповнити":
    amount = int(input("На яку суму ви хочете поповнити: "))
    account.deposit(amount)

else:
    print("Невідома операція")



















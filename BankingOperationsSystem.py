class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance

    def get_details(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added. New balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Withdrawal amount exceeds overdraft limit!")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_savings_account(self, account_number, account_holder):
        if not account_number.isdigit():
            print("Account number should be an integer.")
            return
        acc = SavingsAccount(account_number, account_holder)
        self.accounts.append(acc)
        print("Savings Account created.")

    def create_current_account(self, account_number, account_holder):
        if not account_number.isdigit():
            print("Account number should be an integer.")
            return
        acc = CurrentAccount(account_number, account_holder)
        self.accounts.append(acc)
        print("Current Account created.")

    def get_account_by_number(self, account_number):
        return next((acc for acc in self.accounts if acc.account_number == account_number), None)

    def fund_transfer(self, from_account_number, to_account_number, amount):
        from_acc = self.get_account_by_number(from_account_number)
        to_acc = self.get_account_by_number(to_account_number)

        if from_acc and to_acc:
            if from_acc.get_balance() >= amount:
                from_acc.withdraw(amount)
                to_acc.deposit(amount)
                print("Funds transferred successfully.")
            else:
                print("Insufficient balance in the source account.")
        else:
            print("One or both accounts not found.")

    def get_all_customers(self):
        for acc in self.accounts:
            print(acc.get_details())


def main():
    bank = Bank()

    while True:
        print("\n==== Banking Operations System ====")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Balance Inquiry")
        print("6. Fund Transfer")
        print("7. List All Customers")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            acc_num = input("Enter account number: ")
            if not acc_num.isdigit():
                print("Account number should be an integer.")
                continue
            acc_holder = input("Enter account holder name: ")
            bank.create_savings_account(acc_num, acc_holder)
        elif choice == 2:
            acc_num = input("Enter account number: ")
            if not acc_num.isdigit():
                print("Account number should be an integer.")
                continue
            acc_holder = input("Enter account holder name: ")
            bank.create_current_account(acc_num, acc_holder)
        elif choice == 3:
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            acc = bank.get_account_by_number(acc_num)
            if acc:
                acc.deposit(amount)
            else:
                print("Account not found.")
        elif choice == 4:
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            acc = bank.get_account_by_number(acc_num)
            if acc:
                acc.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == 5:
            acc_num = input("Enter account number: ")
            acc = bank.get_account_by_number(acc_num)
            if acc:
                balance = acc.get_balance()
                print(f"Account balance: {balance}")
            else:
                print("Account not found.")
        elif choice == 6:
            from_acc_num = input("Enter source account number: ")
            to_acc_num = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.fund_transfer(from_acc_num, to_acc_num, amount)
        elif choice == 7:
            bank.get_all_customers()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

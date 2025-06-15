# Comment out the code highlighted in red by enclosing it in triple quotes ("""...""")
class BankAccount:

    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance

accounts = {}

while True:
    print("1. Open a new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        account_no = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        account = BankAccount(account_no, initial_balance)
        accounts[account_no] = account
        print("Account created successfully.")

    elif choice == "2":
        account_no = input("Enter account number: ")
        if account_no not in accounts:
            print("Account does not exist.")
        else:
            amount = float(input("Enter amount to deposit: "))
            try:
                accounts[account_no].deposit(amount)
                print("Deposit successful.")
            except ValueError as e:
                print(e)

    elif choice == "3":
        account_no = input("Enter account number: ")
        if account_no not in accounts:
            print("Account does not exist.")
        else:
            amount = float(input("Enter amount to withdraw: "))
            try:
                accounts[account_no].withdraw(amount)
                print("Withdrawal successful.")
            except ValueError as e:
                print(e)

    elif choice == "4":
        account_no = input("Enter account number: ")
        if account_no not in accounts:
            print("Account does not exist.")
        else:
            balance = accounts[account_no].get_balance()
            print(f"Current balance: {balance:.2f}")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

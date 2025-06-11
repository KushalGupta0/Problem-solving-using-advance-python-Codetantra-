class BankAccount:
    
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance


accounts = {}

while True:
    print("1. Open a new Account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        account_no = input("Enter your account number: ")
        initial_bal = float(input("Enter initial balance: "))
        account = BankAccount(account_no, initial_bal)
        accounts[account_no] = account
        print("Account created successfully.")

    elif choice == '2':
        account_no = input("Enter account number: ")
        if account_no not in accounts:
            print("Account does not exist.")
        else:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print("Deposit successful.")


    elif choice == '3':
        account_no = input("Enter account number: ")
        if account_no not in accounts:
            print("Account does not exist.")
        else:
            amount = float(input("Enter amount to withdraw: "))
            try:
                accounts[account_no].withdraw(amount)
                print("Withdrawal successful.")
            except ValueError as e:
                print(str(e))

    elif choice == '4':
        account_no = input("Enter account number: ")
        if account_no not in accounts:
            print("Account does not exist.")
        else:
            balance = accounts[account_no].get_balance()
            print(f"Current balance: {balance:.2f}")


    elif choice == '5':
        break

    else:
        print("Invalid choice.")
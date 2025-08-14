import random;
class BankAccount:
  def __init__(self, account_holder_name, balance=5000):
    self.account_holder_name = account_holder_name
    self.balance = balance
    self.account_number = random.randint(10**15, 10**16 - 1)

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if amount <= self.balance and self.balance - amount >= 0:
      self.balance -= amount
      return self.balance
    else:
      return "Withdrawal denied: Exceeds balance."

  def display_balance(self):
    return self.balance

class SavingAccount(BankAccount):
  interest_rate = 0.04  # 4%

  def apply_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    return self.balance

class CurrentAccount(BankAccount):
  overdraft_limit = 50000

  def withdraw(self, amount):
    if amount < self.balance and amount <= self.overdraft_limit and self.balance - amount >= 0:
      self.balance -= amount
      return self.balance
    elif amount > self.overdraft_limit:
      return "Withdrawal denied: Exceeds overdraft limit."
    else:
      return "Withdrawal denied: Insufficient funds."

accounttype = input("Enter account type (Saving/Current): ").strip().lower()

if accounttype == "saving":
  accountHolderName = input("Enter account holder name: ")
  initialbalance = float(input("Enter initial balance: "))
  account = SavingAccount(accountHolderName, initialbalance)
elif accounttype == "current":
  accountHolderName = input("Enter account holder name: ")
  initialbalance = float(input("Enter initial balance: "))
  account = CurrentAccount(accountHolderName, initialbalance)
else:
  print("Invalid account type.")
  account = None

if account:
  print("\n      Your account has been created successfully.")
  print(f"      Account Number: {account.account_number}")
  print(f"      Account Holder Name: {account.account_holder_name}")
  print(f"      Initial Balance: {account.balance}")
  if isinstance(account, SavingAccount):
    print(f"      Interest Rate (Bank Fixed): {int(account.interest_rate * 100)}%")
  elif isinstance(account, CurrentAccount):
    print(f"      Overdraft Limit (Bank Fixed): ₹{account.overdraft_limit}")
  
  print("\n      Account Operations:")
  print("      1. Deposit")
  print("      2. Withdraw")
  print("      3. Display Balance")
  print("      4. Exit")

   
  
if account:
  while True:
    operation = input("      Enter operation number (1-4): ").strip()
    if operation == "1":
      amount = float(input("      Enter amount to deposit: "))
      account.deposit(amount)
      print(f"      New balance: {account.display_balance()}")
    elif operation == "2":
      amount = float(input("      Enter amount to withdraw: "))
      result = account.withdraw(amount)
      print(f"      New balance: {result}")

    elif operation == "3":
      result = account.display_balance()
      print(f"      Current balance: {result}")
    elif operation == "4":
      print("      Exiting...")
      break
    else:
      print("      Invalid operation.")
# Practice Question 1
# Create Account Class with 2 attributes - name & account_balance
# Create methods for debit, credit and printing the balance


class Account:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    print("Account created for " + self.name + " with balance " + str(self.balance))

  def deposit(self, amount):
    self.balance += amount
    print("Deposited " + str(amount) + ". New balance is " + str(self.balance))

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print("Withdrew " + str(amount) + ". New balance is " + str(self.balance))
    else:
      print("Insufficient funds. Balance is " + str(self.balance))
    

  def get_balance(self):
    return print("Balance is " + str(self.balance))

Acc1 = Account("Alice",1000)
Acc1.deposit(10000)
Acc1.withdraw(16000)
Acc1.get_balance()
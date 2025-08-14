
class bankAccount:
  amount = 0
  AccountNumber = 1000000000

  def __init__(self, username, password):
    self.username = username
    self.__password = password
    self.AccountNumber = bankAccount.AccountNumber
    bankAccount.AccountNumber += 1 
  
  
  
  def deposit(self, amount):
    self.__amount += amount

  def withdraw(self, amount):
    if amount <= self.__amount:
      self.__amount -= amount
    else:
      print("Insufficient funds")
   
  def get_balance(self):
    return self.__amount
  
  def getPin(self):
    print(self.__pin)
  def setPin(self, pin):
    self.__pin = pin

u1= bankAccount("user1", "pass1")
u1.setPin(8888)
print(u1.get_balance())
u1.deposit(500)
u1.withdraw(200)
print(u1.get_balance())
u1.getPin()
u1.setPin(9999)
u1.getPin()
print(u1.AccountNumber)
u2= bankAccount("user2", "pass2")
print(u2.AccountNumber)
u3= bankAccount("user3", "pass3")
print(u3.AccountNumber)


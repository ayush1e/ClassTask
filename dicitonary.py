
class User:
  name = ""
  age = 0
  def __init__(self, name , age):
    self.name = name
    self.age = age
  def getName(self):
    print("Name: ", self.name)
  def getAge(self):
    print("Age: ", self.age)
  def __str__(self):
    return f"User(name = {self.name}, age = {self.age})"

user1 = User("Alice", 30)
user2 = User("Bob", 25)
user1.getName()
user1.getAge()
user2.getName()
user2.getAge()
print(user1)
print(user2)

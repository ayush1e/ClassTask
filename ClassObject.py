class users:
  def __init__(self, name, password):
    self.name = name
    self.__password = password

  def __setattr__(self, name, value):
    if name == "password":
      self.__password = value
    else:
      self.__dict__[name] = value

  def __getattr__(self, name):
    if name == "password":
      return self.__password
    else:
      return self.__dict__.get(name, None)

user = users("Alice", "pass123")
print(user.__getattr__("password"))

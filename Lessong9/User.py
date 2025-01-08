class User:
  def __init__(self, first_name, last_name, age, city):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.city = city
    self.login_attempts = 0

  def describe_user(self):
    print(f"User's name: {self.first_name} {self.last_name}")
    print(f"User's age: {self.age}")
    print(f"User's city: {self.city}")

  def greet_user(self):
    print(f"Hello {self.first_name} {self.last_name}!")

  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0



user1 = User("John", "Doe", 30, "New York")
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
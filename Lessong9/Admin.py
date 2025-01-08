"""
Администратор. Администратор - особая разновидность пользователя. Напишите класс Admin,
наследуемый от класса User. Добавте атрибут privileges для хранения списка строк вида
"разрешено добавлять сообщения", "разрешено удалять пользователей", 
"разрешено банить пользователей". Напишите метод show_privileges() для вывода
набора привилегий для администратора. Создайте экземпляр Admin и вызовите метод.
"""

from User import User

class Admin(User):
  def __init__(self, first_name, last_name, age, city):
    super().__init__(first_name, last_name, age, city)
    self.privileges = ["разрешено добавлять сообщения", 
                       "разрешено удалять пользователей", 
                       "разрешено банить пользователей"]
    self.show_privileges = Privileges.show_privileges(self, self.privileges)


class Privileges:

  def show_privileges(self, privileges):
    print(self.privileges)


admin = Admin("John", "Doe", 30, "New York")
admin.show_privileges
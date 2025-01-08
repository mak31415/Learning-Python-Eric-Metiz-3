"""
Создайте класс Restaurant. Его метод __init__() должен принимать два атрибута: 
restaurant_name и cuisine_type. Создайте метод describe_restaurant(), который 
выводит два атрибута, и метод open_restaurant(), который сообщение о том что ресторан 
открыт.

Создайте на основе своего класса экземпляр restaurant. Выведите два атрибута по 
отдельности, затем вызовите обе метода.

"""
class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")

  def open_restaurant(self):
    print(self.restaurant_name + " is open.")

  def set_number_served(self, number_served):
    self.number_served = number_served

  def increment_number_served(self, additional_served):
    self.number_served += additional_served


# my_restaurant = Restaurant("Domino's", "Pizza")
# print(my_restaurant.restaurant_name)
# print(my_restaurant.cuisine_type)

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# my_restaurant.number_served = 10
# print("Number served: " + str(my_restaurant.number_served))

# my_restaurant.set_number_served(20)
# print("Number served: " + str(my_restaurant.number_served))

# my_restaurant.increment_number_served(5)
# print("Number served: " + str(my_restaurant.number_served))


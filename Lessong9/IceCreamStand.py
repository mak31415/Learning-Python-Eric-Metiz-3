"""
 Киоск с мороженым. Киоск с мороженым - особая разновидность ре­сторана. 
 Напишите класс IceCreamStand, наследуемый от класса Restaurant из упражнения 9.1 
 или 9.4. Подойдет любая версия класса; просто выберите ту, 
 которая вам больше нравится. Добавьте атрибут flavors для хранения списка 
 сортов мороженого. Напишите метод, который выводит этот список. 
 Создайте экземпляр IceCreamStand и вызовите данный метод.
"""

from Restaurant import Restaurant

class IceCreamStand(Restaurant):
  def __init__(self, restaurant_name, cuisine_type, flavors):
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = flavors

  def describe_flavors(self):
    print(self.flavors)


ice_cream_stand = IceCreamStand("Ice Cream Stand",
                                 "Ice Cream", 
                                 ["chocolate", "vanilla", "strawberry"]) # IceCreamStand


ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_flavors()
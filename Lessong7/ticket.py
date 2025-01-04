"""
Кинотеатр установил несколько вариантов цены на билеьты в зависимости от возвраста 
посетителя. Для посетителя младше 3 лет билет бесплатный, для 3-12 лет стоит 10 долларов, 
а для посетителей старше 12 лет стоит 15 долларов. Напишите цикл, который
предлагает пользователю ввести возвраст и выводит цену билета.
"""

age = int(input("Enter your age: "))

while age != 0:
  if age < 3:
    print("Your ticket is free.")
  elif age < 13:
    print("Your ticket is $10.")
  else:
    print("Your ticket is $15.")

  age = int(input("Enter your age: "))

  if age == 0:
    break

print("End of program.")
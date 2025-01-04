"""
Начните с программы, написаной для упражнения 6.1. 
Создайте два новых словаря, представляющий разных людей и сохраните все три словаря 
списке people. Перебирите элементы списка людей. В процесе перебора выведите всю 
имеющуюся информацию о каждом человеке.
"""

people = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30,
  'city': 'New York'
}

people2 = {
  'first_name': 'Alex',
  'last_name': 'Doe',
  'age': 25,
  'city': 'New York'
}

people3 = {
  'first_name': 'Maria',
  'last_name': 'Doe',
  'age': 30,
  'city': 'New York'
}

peoples = [people, people2, people3]

for people in peoples:
  print(people['first_name'])
  print(people['last_name'])
  print(people['age'])
  print(people['city'])




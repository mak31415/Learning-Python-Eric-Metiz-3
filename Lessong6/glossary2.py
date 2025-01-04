# Создайте словарь с данными о трех больших реках и странах, 
# по которым протекает каждая из этих рек. Одна из возможных 
# пар «ключ - значе­ ние» - 'nile' : 'egypt'.
# • Используйте цикл для вывода сообщения с упоминанием реки 
# и страны - на- пример, «Нил протекает через Египет».
# • Используйте цикл для вывода названия каждой реки, добавленной в словарь.
# • Используйте цикл для вывода названия каждой страны, добавленной в словарь.

rivers = {
  'nile': 'egypt',
  'amazon': 'brazil',
  'mississippi': 'united states',
  'volga': 'russia',
  'yangtze': 'china',
  'yangtze': 'china',
  }

for river, country in rivers.items():
  print(f"The {river.title()} flows through {country.title()}.")

for river in rivers.keys():
  print(river.title())

for country in rivers.values():
  print(country.title())
"""
Создайте словарь cities. Используйте названия городов в качестве ключей словаря.
Создайте словарь с информацией о каждом городе; добавте в него страну, в котором 
расположен город, примерную численность населения и один примечательный факт, относящийся
к этому городу. Ключи словаря должны называтся country, population и fact. Выведите
названия кажлого города и всю сохраненную информацию о нем.
"""

cities = {
  'moscow': {
    'country': 'russia',
    'population': 12000000,
    'fact': 'capital of russia',
    },
  'london': {
    'country': 'united kingdom',
    'population': 9000000,
    'fact': 'capital of england',
    },
  'new york': {
    'country': 'united states',
    'population': 8000000,
    'fact': 'capital of america',
    },
  }

for city, info in cities.items():
  print(f"\nCity: {city.title()}")
  for key, value in info.items():
    print(f"\t{key.title()}: {value}")
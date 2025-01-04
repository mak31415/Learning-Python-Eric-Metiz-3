"""
Напишите функцию city_country(), которая получает название города и страну. Функция
должна возвращать страну и город в формате "London, United Kingdom".
"""

def city_country(city, country):
  return f"{city.title()}, {country.title()}"

print(city_country('moscow', 'russia'))
print(city_country('london', 'united kingdom'))
print(city_country('new york', 'united states'))

print("\n")
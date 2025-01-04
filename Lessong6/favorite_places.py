"""
Создайте словарь favorite_places. Придумайте названия трех мест, которые станут 
ключами словаря, и сохраните для каждого человека из упражнения 6.7 от одного до трех
любимых мест. Переберите данные в словаре, выведите имя каждого человека  
и его любимые места.
"""

favorite_places = {
  'John': ['New York', 'London', 'Paris'],
  'Paul': ['New York', 'London', 'Paris'],
  'George': ['New York', 'London', 'Paris'],
  'Ringo': ['New York', 'London', 'Paris'],
  'Yoko': ['New York', 'London', 'Paris'],
  'Paul McCartney': ['New York', 'London', 'Paris'],}

for name, places in favorite_places.items():
  print(f"\n{name.title()}'s favorite places are:")
  for place in places:
    print(f"\t{place.title()}")
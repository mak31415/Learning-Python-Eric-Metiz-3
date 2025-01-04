favorites_numbers = {
  'John': [1, 2, 3],  
  'Paul': [4, 5,],
  'George': [7, 8, 9],
  'Ringo': [10, ],
  'Yoko': [13, 14,],
  'Paul McCartney': [16, 17, 18]
  }

for name, numbers in favorites_numbers.items():
  print(f"\n{name.title()}'s favorite numbers are:")
  for number in numbers:
    print(f"\t{number}")
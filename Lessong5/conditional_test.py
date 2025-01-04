car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'bmw'? I predict True.")
print(car != 'bmw')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\n")

age = 18

if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote yet?")
  print("Did you vote in the last election?")

if age < 18:
  print("You are not 18 years old.")

print("\n")

if 'audi'.lower() in cars:
  print("Audi is in the list.")

print("\n")

if 'bmw'.lower() not in cars:
  print("Bmw is not in the list.")

if 'audi'.lower() not in cars or 'bmw'.lower() not in cars:
  print("Audi or Bmw is not in the list.")
guests = ['John', 'Paul', 'George', 'Ringo']

print("\n")

print("I'm inviting " + str(len(guests)) + " people to dinner.")

for guest in guests:
  print("Hello " + guest + ", would you like to join me for dinner?")

guests.remove('Ringo')

guests.append('John Lennon')

print("\n")

print("I'm inviting " + str(len(guests)) + " people to dinner.")

for guest in guests:
  print("Hello " + guest + ", would you like to join me for dinner?")


print("\n")

guests.insert(0, 'Paul McCartney')
guests.insert(2, 'George Harrison')
guests.append('Yoko Ono')

print("I'm inviting " + str(len(guests)) + " people to dinner.")

while guests:
  guest = guests.pop()
  print("Hello " + guest + ", would you like to join me for dinner?")

print("\n")

print("I'm inviting " + str(len(guests)) + " people to dinner.")

guests = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Yoko Ono']

guests.clear()

print("I'm inviting " + str(len(guests)) + " people to dinner.")
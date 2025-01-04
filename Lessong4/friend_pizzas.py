my_pizzas = ['pepperoni', 'mushrooms', 'extra cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.append('bacon')
friend_pizzas.append('pineapple')

print("My favorite pizzas are:")
for pizza in my_pizzas:
  print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(pizza)
order = input("How many seats do you want to reserve in the restaurant: ")

if int(order) > 8:
  print("You will need to wait for a table.")
else:
  print("Your table is ready.")
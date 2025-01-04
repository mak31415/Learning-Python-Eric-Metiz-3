"""
Создайте список sandwich_orders, заполните его названиями различных бутербродов.
Создайте пустой список finished_sandwiches. В цикле переберите элементы первого списка
и выведите сообщение для каждого элемента (например, "Я приготовил бутерброд с тунцом").
После этого каждый бутерброд из первого списка перемещается в список finished_sandwiches.
После того как все элементы первого списка будут обработаны, выведите сообщение, в 
котором перечисляются названия всех изготовленных бутербродов. 
"""

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
  current_sandwich = sandwich_orders.pop()
  print(f"I made a {current_sandwich.title()} sandwich.")
  finished_sandwiches.append(current_sandwich)

print("\nThese sandwiches have been made:")
for sandwich in finished_sandwiches:
  print(f"\t{sandwich.title()}")
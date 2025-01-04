"""
Бутерброды.
Напишите функцию, которая получает список компонентов бутерброда. Функция должна
иметь один параметр для любого количества значений, переданных при вызове функции, и
выводит описания заказанного бутерброда. Вызовите функцию три раза с разными 
количествами аргументов.
"""

def make_sandwich(*ingredients):
  print("\nMaking a sandwich with the following ingredients:")
  for ingredient in ingredients:
    print("- " + ingredient)

make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'bacon')
make_sandwich('peanut butter', 'jelly', 'banana')
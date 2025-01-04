"""
Используя список sandwich_orders из предыдущего упражнения, проследите за тем, чтобы 
значение 'pastrami' встречалось в списке минимум три раза. Добавте в начало программы 
код для вывода сообщения о том, что пастромы больше нет, и напишите цикл while, 
удаляющий все вхождения 'pastrami' из списка sandwich_orders. Убедитесь в том, что
в finished_sandwiches значение 'pastrami' не встречается ни одного раза.   
"""

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'pastrami', 
                   'pastrami', 'tuna', 'cheese']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
  finished_sandwiches.append(sandwich)

print("\nThese sandwiches have been made:")
print(finished_sandwiches) 

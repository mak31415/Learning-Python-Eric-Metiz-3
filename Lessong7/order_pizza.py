"""
Три выхода. Напишите альтернативную версию упражнения 7.4. или упражнения 7.5.
в которой каждый пункт следующего списка встречается хотя бы раз:

1. завершение цикла пр проверке условия в операторе while.
2. управление продолжительностью цикла в зависимости от переменной active.
3. выход из цикла с помощью оператора break, если пользователь вводит 'quit'.
"""

order = []

active = True

while active:
    pizza = input("What kind of pizza do you want? ")

    if pizza == 'quit':
        break  # Выход из цикла с помощью оператора break
    else:
        order.append(pizza)

if order:  # Проверяем, есть ли в списке что-то (order != [] эквивалентно bool(order))
    for pizza in order:
        print("I will prepare your " + pizza + " pizza.")


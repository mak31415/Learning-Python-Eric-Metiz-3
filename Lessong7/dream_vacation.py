"""
Отпуск мечты. Напишите программу, которая спрашивает пользователей, где бы они хотели
провести отпуск. Добавте подсказку вида "Если бы вы могли посетить одно место в мире,
то куда бы вы отправились?" Добавте блок кода, который выводит результаты опроса.
"""

question = "If you could visit one place in the world, where would you go?"
prompt = "Enter the name of the place: "

place = input(question + " " + prompt)
print("Your dream vacation is to visit " + place + ".")
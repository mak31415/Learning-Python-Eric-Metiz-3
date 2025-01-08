"""
Гостевая книга. Напишите цикл while, который в цикле запрашивает у пользователей имена.
При выводе каждого имени выведите на экран приветствие и добавте строку с сообщением 
в файл guest_book.txt. Проследите за тем чтобы каждое сообщение было на отдельной строке.
"""

from pathlib import Path

contents = ''

while True:
  guest = input("What is your name? ")

  if guest == 'quit':
    break

  path = Path('Lessong10/guest_book.txt')
  contents +=  guest + "\n"

  print("Hello " + guest + ", would you like to learn some Python today?")


path = Path('Lessong10/guest_book.txt')
contents = path.write_text(contents)
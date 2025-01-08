"""
Кошки и собаки. Создайте два файла с именами cats.txt и dogs.txt. Сохраните по 
крайней мере три клички кошек и собак. Напишите программу, которая пытается прочитать
эти файлы и выводит их содержимое на экран. Поместите вой код в блок try- except в целях
перехвата исключения FileNotFoundError и вывода понятного сообщения об отсутствии файла.
Переместите один из файлов в другое место файловой системы; убедитесь в том, что
блок кода exept работает правильно. 
"""

from pathlib import Path

path = ['Lessong10/cats.txt', 'Lessong10/dogs.txt']

try:
  for file in path:
    path = Path(file)
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
  print("Sorry, the file you are looking for does not exist.")

else:
  print("Good job!")
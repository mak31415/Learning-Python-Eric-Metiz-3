"""
Считает количество слов в файле."""

from pathlib import Path

path = Path('Lessong10/Alice.txt')

try:
  contents = path.read_text()
except FileNotFoundError:
  print("Sorry, the file you are looking for does not exist.")
else:
  words = contents.split()
  num_words = len(words)
  print("The file " + 
        str(path) + 
        " has about " + 
        str(num_words) 
        + " words.")
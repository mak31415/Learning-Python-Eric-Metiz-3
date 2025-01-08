from pathlib import Path

path = Path('Lessong10/learning_python.txt')
contents = path.read_text()

contents = contents.replace('dogs', 'cats')

print(contents)
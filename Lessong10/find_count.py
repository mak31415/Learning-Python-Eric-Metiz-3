from pathlib import Path


def count_words(filename):
  """Count the approximate number of words in a file."""
  try:
    contents = Path(filename).read_text()
  except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
  else:
    words = contents.lower().split()
    num_words = words.count('alice')
    print(f"The file {filename} has about {num_words} mentions of Alice.")


filename = 'Lessong10/Alice.txt'
count_words(filename)
from pathlib import Path
import json

def favorite_numbers():
  path = Path('Lessong10/favorite_numbers.json')
  if path.exists():
    contents = path.read_text()
    favorite_numbers = json.loads(contents)
    print("Your favorite numbers are: " + favorite_numbers) 
  else:
    favorite_numbers = input("What are your favorite numbers? ")
    contents = json.dumps(favorite_numbers)
    path.write_text(contents)
    print("Your favorite numbers are: " + favorite_numbers)

favorite_numbers()
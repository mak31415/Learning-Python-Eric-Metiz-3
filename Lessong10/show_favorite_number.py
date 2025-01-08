from pathlib import Path
import json

path = Path('Lessong10/favorite_numbers.json')
contents = path.read_text()
favorite_numbers = json.loads(contents)

print("Your favorite numbers are: " + str(favorite_numbers))
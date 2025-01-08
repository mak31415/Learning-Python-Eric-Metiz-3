from pathlib import Path
import json


path = Path('Lessong10/username.json')
contents = path.read_text()
user_name = json.loads(contents)

print(user_name.get('first') + " " + user_name.get('last'))

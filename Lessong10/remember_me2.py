from pathlib import Path
import json

def get_stored_username(path):
  """Возвращает сохраненное имя пользователя, если оно существует."""
  if path.exists():
    contents = path.read_text()
    user_name = json.loads(contents)
    return user_name
  else:
    return None
  
def get_new_username(path):
  """Запрашивает новое имя пользователя."""
  first_name = input("What is your name? ")
  last_name = input("What is your last name? ")
  user_name = {'first': first_name, 'last': last_name}
  contents = json.dumps(user_name)
  path.write_text(contents)
  return user_name

def greet_user():
  """Приветствует пользователя по имени."""

  path = Path('Lessong10/username.json')
  user_name = get_stored_username(path)

  if user_name:
    first_name = input("What is your name? ")
    last_name = input("What is your last name? ")
    if first_name == user_name['first'] and last_name == user_name['last']:
      print("Welcome back, " + user_name['first'] + " " + user_name['last'] + "!")
  else:
    user_name = get_new_username(path)
    print("We'll remember you when you come back, " + user_name['first'] + 
          " " + user_name['last'] + "!")

greet_user()
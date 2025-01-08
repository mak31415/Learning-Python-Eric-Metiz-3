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
  user_name = input("What is your name? ")
  contents = json.dumps(user_name)
  path.write_text(contents)
  return user_name

def greet_user():
  """Приветствует пользователя по имени."""

  path = Path('Lessong10/username.json')
  user_name = get_stored_username(path)

  if user_name:
    print("Welcome back, " + user_name + "!")
  else:
    user_name = get_new_username(path)
    print("We'll remember you when you come back, " + user_name + "!")

greet_user()
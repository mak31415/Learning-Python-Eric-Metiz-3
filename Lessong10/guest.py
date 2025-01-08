from pathlib import Path

guest = input("What is your name? ")

path = Path('Lessong10/guest.txt')
contents = path.write_text(guest)

print("Hello " + guest + ", would you like to learn some Python today?")

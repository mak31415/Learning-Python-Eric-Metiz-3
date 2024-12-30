# This program prints out some of the most common name cases

name = input("Please enter your name: ")
print("Hello " + name.title() + ", would you like to learn some Python today?")
print("Hello " + name.lower() + ", would you like to learn some Python today?")
print("Hello " + name.upper() + ", would you like to learn some Python today?")

print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")

famous_person = "Albert Einstein"
message = f"{famous_person} once said, \"A person who never made a mistake never tried anything new.\""
print(message)

user = " Albert Einstein "
print(user)
print(user.lstrip())
print(user.rstrip())
print(user.strip())

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
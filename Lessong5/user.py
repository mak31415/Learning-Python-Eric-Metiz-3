current_user = ['admin', 'eric', 'john', 'mary', 'bob']

new_user = [ 'eric',  'mary', 'alice', 'max', 'alex']

for user in new_user:
  if user in current_user:
    print("The username " + user + " is already taken. Please enter a new username.")
  else:
    print("The username " + user + " is available.")


name = 'ERIC'
name2 = 'Eric'

result = name == name2
print(result)
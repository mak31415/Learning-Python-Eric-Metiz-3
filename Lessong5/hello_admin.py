user = ['admin', 'eric', 'john', 'mary', 'bob']


if user == []:
  print("We need to find some users!")
else:
  for user_name in user:
    if user_name == 'admin':
      print("Hello admin, would you like to see a status report?")
    else:
      print("Hello " + user_name + ", thank you for logging in again.")
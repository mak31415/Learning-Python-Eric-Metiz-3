numbers = []

for value in range(1, 21):
  numbers.append(value)

print(numbers)

numbers_list = [value for value in range(1, 21)]
print(numbers_list)

numbers_list = [value for value in range(1, 21) if value % 2 == 0]
print(numbers_list)
"""
Напиши функцию two_sum, принимающую список целых чисел nums, целое число 
target и возвращает индексы двух чисел из списка, если их сумма равна target.
Индексы должны быть отсортированы в порядке возрастания.
two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1] # 2 + 7 = 9
two_sum(nums=[3, 2, 4], target=6) == [1, 2] # 2 + 4 = 6
"""

def two_sum(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
      

print(two_sum([2, 7, 11, 15], 9))


def describe_city(city, country='Russia'):
  print(city + " is in " + country)

describe_city('Moscow')
describe_city('London', 'United Kingdom')
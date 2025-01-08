import random

class Die:
  def __init__(self, num_sides=6):
    self.num_sides = num_sides

  def roll_die(self):
    return random.randint(1, self.num_sides)
  

throw = Die()
print(throw.roll_die())

throw = Die(10)
print(throw.roll_die())

throw = Die(20)
print(throw.roll_die())
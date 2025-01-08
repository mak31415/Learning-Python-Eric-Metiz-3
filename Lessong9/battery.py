class Battery:
  def __init__(self, battery_size=70):
    self.battery_size = battery_size

  def describe_battery(self):
    print(f"This car has a {self.battery_size}-kWh battery.")

  def get_range(self):
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270
    message = f"This car can go approximately {range} miles on a full charge."
    print(message)

  def upgrade_battery(self):
    if self.battery_size < 65:
      self.battery_size = 65

  
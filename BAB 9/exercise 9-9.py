class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Baterai: {self.battery_size} kWh")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"Jarak tempuh: {range} mil")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar("Nissan", "Leaf", 2024)

my_car.battery.describe_battery()
my_car.battery.get_range()

print("\nSetelah upgrade baterai:")

my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()
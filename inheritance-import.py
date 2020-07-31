from inheritance import ElectricCar, Battery

my_car_1 = ElectricCar('Tesla', 'model t', 2020)
my_car_1.battery.describe_battery()

my_car_1 = Battery(100)
my_car_1.describe_battery()

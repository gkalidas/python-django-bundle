class Car():
    """ Information about the car """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km_reading = 14
        # default value for km

    def get_des(self):
        """ This function prints the information about the car """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_km(self):
        """ This function reads and prints the car km """
        print('This car has', self.km_reading, 'km on it.')

    def update_km(self, km):
        """ This function updates the km of the car """
        if km >= self.km_reading:
            self.km_reading = km
        else:
            print("You can't roll back on km.")


class ElectricCar(Car):
    """
    This class inherites from Car class.
    Will have his own methods soon.
    """
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def desc_battery(self):
        """This function describes the battery."""
        print('This car has ' + str(self.battery) + ' kwh battery.')

    def fill_gas(self):
        print("This car doesn't need gas tank.")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """This function describes/prints the battery size of a given model."""
        print("This car has a " + str(self.battery_size) + "kwh battery.")


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_des())
# my_new_car.read_km()
# my_new_car.update_km(13)
# my_new_car.read_km()

# my_car = ElectricCar('Tesla', 'model s', 2019)
# print(my_car.get_des())
# my_car.desc_battery()

# importing battery from Battery class
# my_car.battery.describe_battery()
# my_car.fill_gas()

my_car_1 = ElectricCar('Tesla', 'model t', 2020)
my_car_1.battery.describe_battery()
my_car_1 = Battery(100)
my_car_1.describe_battery()

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


my_new_car = Car('audi', 'a4', 2016)

print(my_new_car.get_des())
my_new_car.read_km()
my_new_car.update_km(13)
my_new_car.read_km()

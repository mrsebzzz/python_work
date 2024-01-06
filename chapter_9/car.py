class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2000

    def get_descriptive_name(self):
        """Return a neatly formatted name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self, mileage):
        """Set the odometer and reject if attempted to roll back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the miles!")

    def read_odometer(self):
        """Print a statement showing the cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
my_new_car = Car('audi', 'a4', '2024')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(1000)
my_new_car.read_odometer()

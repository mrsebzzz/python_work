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

    def increment_odometer(self, miles):
        """Add the give amount to the odometer"""
        self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

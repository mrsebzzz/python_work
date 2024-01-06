class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurants name is {self.restaurant_name}.")
        print(f"The cuisine type is: {self.cuisine_type}.")

    def restaurant_open(self):
        print(f"The {self.restaurant_name} is open!")

my_restaurant = Restaurant('Seppys', 'Pizza')
your_restaurant = Restaurant('Laynes', 'Potatos')

print(f"My dogs name is {my_restaurant.restaurant_name}.")
print(f"My dog is {my_restaurant.cuisine_type} years old")
my_restaurant.restaurant_open()

print(f"My dogs name is {your_restaurant.restaurant_name}.")
print(f"My dog is {your_restaurant.cuisine_type} years old")
your_restaurant.restaurant_open()
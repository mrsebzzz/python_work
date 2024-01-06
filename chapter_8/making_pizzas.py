import pizza_two

pizza_two.make_pizza(16, 'pepperoni')
pizza_two.make_pizza(12, 'cheese','peppers', 'sausage')

# import specific functions
from pizza_two import make_pizza

# giving the function an alias
from pizza_two import make_pizza as mp

# giving the module an alias
import pizza_two as p

p.make_pizza('14', 'alias')

#importing all functions in a module
from pizza_two import *

# styling functions

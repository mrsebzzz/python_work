def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#summarize the pizza we are making

def make_pizza(*toppings):
    """Summarize"""
    print("\nMake a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize"""
    print(f"\nMaking a {size} pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(14, 'shrooms', 'peppers', 'cheese')
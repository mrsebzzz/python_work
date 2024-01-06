def make_pizza(size, *toppings):
    """Summarize the pizza"""
    print(f"\nMaking a {size} pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
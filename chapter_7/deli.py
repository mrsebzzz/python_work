sandwich_orders = ['beef', 'veggie', 'sausage', 'cheese', 'vegan']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"Finished making sandwich: {current_order.title()}")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches are complete:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title()) 

print(finished_sandwiches)
print(sandwich_orders)
import printing_functions as pf

# Modifying a list in a function
# start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate print each design, until none are left
# move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# display all completed models.
print("\nThe following models have been completed: ")
for completed_model in completed_models:
    print(completed_model)

print("\n\nThis is the better way below")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
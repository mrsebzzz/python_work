# reorganize this code by writing two functions
def print_models(unprinted_designs, completed_models):
    """Simulate printing each model"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been completed: ")
    for completed_model in completed_models:
        print(completed_model)
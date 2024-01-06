# Positional arguements
def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'tyson')

# Multiple function calls
describe_pet('hamser', 'sally')

# Order matters in positional argurments
describe_pet('sebastian', 'cat')

# Keyword arguments, order doesn't matter. telling python exactly what you want
# same output even when switched around
describe_pet(animal_type='cat', pet_name='sebastian')
describe_pet(pet_name='sebastian', animal_type='cat')



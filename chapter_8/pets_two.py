# Default values
def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('sebastian')

# can still be modified within the function call
describe_pet('josh', animal_type='cat')

# equivalent function calls, same outputs
def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# same ouputs
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named harry, same outputs
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# avoiding argument errors
describe_pet()
def greet_user(username):
    """Display a simple greeting."""
    print(f"hello!, {username.title()}")

greet_user('jesse')

# using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is in infinite loop, until you put in the quit statements
while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to exit program.)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
# Passing a list
def greet_users(names):
    """Print a simple message greeting each user on a list"""
    for name in names:
        msg =f"hello {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
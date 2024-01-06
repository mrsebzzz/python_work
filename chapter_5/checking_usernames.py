current_users = ['admin', 'level one', 'level two', 'moderator', 'noob']
new_users = ['admin', 'sparky', 'corey', 'moderator', 'jones']


for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} you need a new name")
    else:
        print(f"{new_user} that name is available.")


# ordinal numbers
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
    if number == '1':
        print(f"\n{number}st")
    elif number == '2':
        print(f"\n{number}nd")
    elif number == '3':
        print(f"\n{number}rd")
    elif number > '3':
        print(f"\n{number}th")
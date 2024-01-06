usernames = ['admin', 'level one', 'level two', 'moderator', 'noob']
user = 'admin'

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin!")
else:
    print("we need some users")
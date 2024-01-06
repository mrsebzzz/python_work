banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

if user in banned_users:
    print(f"{user.title()}, you're banned.")


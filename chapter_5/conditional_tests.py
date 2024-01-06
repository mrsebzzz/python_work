#exercises
car = 'subaru'
print("Is car == 'subuaru'? I predict true")
print(car == 'subaru')

print("\nIs car == audi? I predict false")
print(car == 'audi')

print("\n")
number = 17
print(number != 17)
print(number == 17)
print(16 > 17)
print(1 < 17)


answer = 42
if answer == 42:
    print("\nThe secret to life!")

banned_users = ['josh', 'kevin', 'mike', 'layne']
user = 'josh'
user_two = 'josh'

if user in banned_users:
    print("you are banned")
if user not in banned_users:
    print("you are not banned")

age_0 = 21
age_1 = 42
if age_0 > 3 or age_1 < 80:
    print("true")
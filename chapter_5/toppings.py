requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

if requested_topping == 'mushrooms':
    print("Put Shrooms on that!")

# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza")

# wouldn't work with an if-elif-else statement, see below

if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza")
print("\n")

# using if statements with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry we are out of {requested_topping}.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making pizza.")

# checking to see if a list is empty

print("\n")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making pizza.")
else:
    print("Are you sure you want a plain pizza?")
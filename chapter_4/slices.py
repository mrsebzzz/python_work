#exercises with slices
my_foods = ['pizza','falafel','carrot cake', 'seeds', 'jerky']
print(my_foods[0:2]) #beginning
print(my_foods[2:4]) #middle
print(my_foods[-3:]) #last three

#pizza exercise, adding to different lists
my_pizzas = ['cheese', 'sausage', 'pepperoni']
friends_pizzas = my_pizzas[:]

my_pizzas.append('anchiove')
friends_pizzas.append('pineapple')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"\t{pizza}")

print("My friend likes these:")
for pizza in friends_pizzas:
    print(f"\t{pizza}")
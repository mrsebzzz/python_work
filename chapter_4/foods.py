my_foods = ['pizza','falafel','carrot cake']
friends_food = my_foods[:]

#this doesnt work, use the slice above instead
#freinds_foods = my_foods

my_foods.append('watermelon')
friends_food.append('ice cream')

print("My favorite foods are:")
print(f"\t{my_foods}")

print("\nMy friend's favorite foods are:")
print(f"\t{friends_food}")

#extended exercise to writel oops
print("My favorite foods are:")
for food in my_foods:
    print(f"\t{my_foods}")
print("\nMy friend's favorite foods are:")
for food in friends_food:
    print(f"\t{friends_food}")
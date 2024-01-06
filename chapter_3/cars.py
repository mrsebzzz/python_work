#using sort will permanently change the order
cars = ['bmw', 'toyota', 'mercedes', 'ford']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


#using sorted will keep the original list in order but print it differently.
cars = ['bmw', 'toyota', 'mercedes', 'ford']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("test")
#printing a list in reserver order
cars = ['bmw', 'toyota', 'mercedes', 'ford']
print(cars)
cars.reverse()
print(cars)
#reverse changes the list permanently but you can just reverse it back.
cars.reverse()
print(cars)


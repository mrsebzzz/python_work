dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#this will throw an error
#dimensions[0] = 250

#tuple with one element needs a trailing comma
my_t = (3,)
print(my_t[0])

#looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

#writing over a Tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

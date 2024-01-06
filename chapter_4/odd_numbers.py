odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

for value in range(1, 21):
    print(value + 2)

#threes
threes = [value*3 for value in range (1,31)]
print(threes)

#cube
cubes = []
for value in range (1,21):
    cubes.append(value**3)
print(cubes)

#cube comprehension
cubes = [value**3 for value in range (1,21)]
print(cubes)
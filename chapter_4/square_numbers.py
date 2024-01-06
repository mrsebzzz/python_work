#square numbers in a range, listed
square_numbers = []
for value in range (1, 11):
    square = value ** 2
    square_numbers.append(square)

print(square_numbers)

#more concise way
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#even more concise, one line of code. list comprehensions
squares = [value**2 for value in range (1,11)]
print(squares)
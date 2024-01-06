number = input(
    "Please enter a number, I will tell you if its a multiple of ten ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of ten")
else:
    print(f"The number {number} is NOT a multiple of ten")
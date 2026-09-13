"""Program 1.23: sums of natural numbers, squares and cubes."""
number = int(input("Enter N: "))
natural = squares = cubes = 0
for value in range(1, number + 1):
    natural += value
    squares += value ** 2
    cubes += value ** 3
print("Natural number sum:", natural)
print("Square sum:", squares)
print("Cube sum:", cubes)

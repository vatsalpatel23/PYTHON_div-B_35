"""Program 2.3: factorial table using a function."""
def factorial(number):
    result = 1
    for value in range(2, number + 1): result *= value
    return result

print("Number  Factorial")
for number in range(1, 11): print(number, "=", factorial(number))

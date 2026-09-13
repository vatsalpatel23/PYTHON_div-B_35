factorial = lambda number: 1 if number <= 1 else number * factorial(number - 1)
number = int(input('Enter number: '))
print(factorial(number))

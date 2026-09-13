def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result
number = int(input('Enter a non-negative number: '))
if number >= 0:
    print('Factorial:', factorial(number))
else:
    print('Factorial is not defined for negative numbers.')

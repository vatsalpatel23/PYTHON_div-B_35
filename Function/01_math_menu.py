def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def floor_divide(a, b):
    return a // b

def power(a, b):
    return a ** b
operations = {'1': add, '2': subtract, '3': multiply, '4': divide, '5': floor_divide, '6': power}
print('1 Add  2 Subtract  3 Multiply  4 Divide  5 Integer Divide  6 Power')
choice = input('Choose: ')
a = float(input('First number: '))
b = float(input('Second number: '))
if choice in operations:
    try:
        print('Result:', operations[choice](a, b))
    except ZeroDivisionError:
        print('Cannot divide by zero.')
else:
    print('Invalid choice.')

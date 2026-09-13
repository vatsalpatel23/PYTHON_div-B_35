numbers = [int(value) for value in input('Enter numbers: ').split()]
positive = [number for number in numbers if number > 0]
negative = [number for number in numbers if number < 0]
zero = [number for number in numbers if number == 0]
print('Positive:', positive)
print('Negative:', negative)
print('Zero:', zero)

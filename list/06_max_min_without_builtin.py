numbers = [25, 8, 42, 16, 3, 31]
largest = smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print('Maximum:', largest)
print('Minimum:', smallest)

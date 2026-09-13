numbers = [int(value) for value in input('Enter numbers separated by spaces: ').split()]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print('Unique list:', unique)

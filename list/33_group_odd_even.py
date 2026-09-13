numbers = [1, 2, 3, 4, 5, 6]
groups = {'even': [], 'odd': []}
for number in numbers:
    if number % 2 == 0:
        groups['even'].append(number)
    else:
        groups['odd'].append(number)
print(groups)

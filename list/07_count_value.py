numbers = [10, 20, 10, 30, 10, 40]
value = int(input('Enter value to count: '))
count = 0
for number in numbers:
    if number == value:
        count += 1
print('Occurrences:', count)

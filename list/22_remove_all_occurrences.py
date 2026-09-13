numbers = [1, 2, 3, 2, 4, 2, 5]
value = int(input('Enter value to remove: '))
result = []
for number in numbers:
    if number != value:
        result.append(number)
print(result)

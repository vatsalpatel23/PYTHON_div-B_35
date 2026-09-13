numbers = [5, -2, 10, -8, 0, 3]
for index in range(len(numbers)):
    if numbers[index] < 0:
        numbers[index] = 0
print(numbers)

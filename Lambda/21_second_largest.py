numbers = [12, 45, 7, 31, 20, 45]
largest = max(numbers)
second_largest = max(filter(lambda number: number < largest, numbers))
print(second_largest)

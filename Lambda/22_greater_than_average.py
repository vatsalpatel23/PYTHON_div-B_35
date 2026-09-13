numbers = [12, 45, 7, 31, 20]
average = sum(numbers) / len(numbers)
result = list(filter(lambda number: number > average, numbers))
print(result)

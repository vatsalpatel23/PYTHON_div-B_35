numbers = [10, 15, 20, 30, 45, 50, 60]
result = list(filter(lambda number: number % 3 == 0 and number % 5 == 0, numbers))
print(result)

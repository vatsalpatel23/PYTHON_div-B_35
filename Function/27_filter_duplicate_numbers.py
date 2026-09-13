numbers = [1, 2, 2, 3, 4, 4, 5]
result = list(filter(lambda number: numbers.count(number) == 1, numbers))
print(result)

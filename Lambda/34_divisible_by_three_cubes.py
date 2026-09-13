numbers = [1, 2, 3, 4, 5, 6, 9]
divisible = filter(lambda number: number % 3 == 0, numbers)
result = list(map(lambda number: number ** 3, divisible))
print(result)

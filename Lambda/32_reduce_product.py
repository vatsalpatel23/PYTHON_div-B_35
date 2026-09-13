from functools import reduce
numbers = [2, 3, 4, 5]
result = reduce(lambda first, second: first * second, numbers)
print(result)

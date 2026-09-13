from functools import reduce
numbers = [10, 20, 30, 40]
result = reduce(lambda first, second: first + second, numbers)
print(result)

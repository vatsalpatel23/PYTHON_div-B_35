from functools import reduce
numbers = [12, 45, 7, 31, 20]
result = reduce(lambda first, second: first if first > second else second, numbers)
print(result)

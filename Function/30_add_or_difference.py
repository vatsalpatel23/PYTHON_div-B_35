first = [6, 5, 3, 9]
second = [0, 1, 7, 7]
result = list(map(lambda pair: pair[0] + pair[1] if pair[0] > pair[1] else pair[1] - pair[0], zip(first, second)))
print(result)

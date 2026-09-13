combine = lambda first, second: first * second if type(first) == int and type(second) == int else str(first) + str(second)
print(combine(4, 5))
print(combine('Hello ', 'Python'))

items = [10, 'Python', 20, 'List', 30.5, 40]
integers = list(filter(lambda item: type(item) == int, items))
print(integers)

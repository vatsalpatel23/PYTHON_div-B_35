nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for row in nested:
    for value in row:
        flat.append(value)
print(flat)

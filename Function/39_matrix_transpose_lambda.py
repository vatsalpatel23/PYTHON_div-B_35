matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = lambda rows: [list(column) for column in zip(*rows)]
print(transpose(matrix))

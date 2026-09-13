"""Program 3.8: 3x3 matrix operations."""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:")
for row in matrix: print(*row, sep="\t")
for index, row in enumerate(matrix, 1): print("Row", index, "sum:", sum(row))
print("Main diagonal sum:", sum(matrix[i][i] for i in range(3)))

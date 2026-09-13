first = [[1, 2], [3, 4]]
second = [[5, 6], [7, 8]]
addition = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(first[i][j] + second[i][j])
    addition.append(row)
transpose = [[first[j][i] for j in range(2)] for i in range(2)]
print('Addition:', addition)
print('Transpose:', transpose)
print('Row sums:', [sum(row) for row in first])
print('Column sums:', [first[0][i] + first[1][i] for i in range(2)])

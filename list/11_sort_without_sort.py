numbers = [45, 12, 7, 31, 20]
ascending = numbers[:]
for i in range(len(ascending)):
    for j in range(len(ascending) - 1):
        if ascending[j] > ascending[j + 1]:
            ascending[j], ascending[j + 1] = (ascending[j + 1], ascending[j])
descending = ascending[::-1]
print('Ascending:', ascending)
print('Descending:', descending)

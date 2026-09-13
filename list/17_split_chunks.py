numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = int(input('Enter chunk size: '))
chunks = []
for index in range(0, len(numbers), size):
    chunks.append(numbers[index:index + size])
print(chunks)

numbers = [2, 4, 3, 5, 7, 8, 1]
target = int(input('Enter target sum: '))
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])

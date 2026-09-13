numbers = [int(value) for value in input('Enter numbers: ').split()]
k = int(input('Enter k: ')) % len(numbers)
print('Left:', numbers[k:] + numbers[:k])
print('Right:', numbers[-k:] + numbers[:-k])

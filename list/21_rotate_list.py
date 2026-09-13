numbers = [1, 2, 3, 4, 5]
positions = int(input('Enter positions: ')) % len(numbers)
print('Left:', numbers[positions:] + numbers[:positions])
print('Right:', numbers[-positions:] + numbers[:-positions])

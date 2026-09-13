numbers = [1, 2, 1, 3, 2, 1]
frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1
print(frequency)

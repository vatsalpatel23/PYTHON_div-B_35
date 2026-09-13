numbers = [100, 4, 200, 1, 3, 2, 5]
values = set(numbers)
longest = 0
for number in values:
    if number - 1 not in values:
        length = 1
        while number + length in values:
            length += 1
        if length > longest:
            longest = length
print('Longest consecutive length:', longest)

numbers = [1, 2, 4, 7, 8, 10]
missing = []
for number in range(min(numbers), max(numbers) + 1):
    if number not in numbers:
        missing.append(number)
print(missing)

first = [1, 2, 3, 4, 5]
second = [3, 4, 6]
result = []
for number in first:
    if number not in second:
        result.append(number)
print(result)

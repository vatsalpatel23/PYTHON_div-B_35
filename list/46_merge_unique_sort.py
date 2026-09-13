first = [5, 2, 8, 2]
second = [3, 8, 1, 5]
merged = []
for number in first + second:
    if number not in merged:
        merged.append(number)
merged.sort()
print('Ascending:', merged)
print('Descending:', merged[::-1])

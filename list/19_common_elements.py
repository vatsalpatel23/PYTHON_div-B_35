first = [1, 2, 3, 4, 5]
second = [3, 4, 5, 6, 7]
common = []
for number in first:
    if number in second and number not in common:
        common.append(number)
print(common)

numbers = [12, 45, 7, 31, 20, 45]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
unique.sort()
print('Second smallest:', unique[1])
print('Second largest:', unique[-2])

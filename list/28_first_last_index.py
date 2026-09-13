numbers = [10, 20, 30, 20, 40, 20]
value = int(input('Enter value: '))
first = -1
last = -1
for index in range(len(numbers)):
    if numbers[index] == value:
        if first == -1:
            first = index
        last = index
print('First index:', first)
print('Last index:', last)

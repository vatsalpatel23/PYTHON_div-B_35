numbers = [25, 10, 45, 5, 30]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Maximum =", maximum)
print("Minimum =", minimum)
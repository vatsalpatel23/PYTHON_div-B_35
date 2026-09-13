numbers = [12, 45, 7, 31, 20, 45]
largest = second_largest = float('-inf')
smallest = second_smallest = float('inf')
for number in numbers:
    if number > largest:
        second_largest, largest = (largest, number)
    elif largest > number > second_largest:
        second_largest = number
    if number < smallest:
        second_smallest, smallest = (smallest, number)
    elif smallest < number < second_smallest:
        second_smallest = number
print('Second largest:', second_largest)
print('Second smallest:', second_smallest)

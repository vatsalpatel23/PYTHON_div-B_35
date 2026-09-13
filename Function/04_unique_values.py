def unique_values(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result
sample = [1, 2, 3, 3, 3, 3, 4, 5]
print(unique_values(sample))

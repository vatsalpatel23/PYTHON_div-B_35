numbers = [5, 2, 8, 2, 5, 1, 3]
indexed_numbers = enumerate(numbers)
unique_pairs = filter(lambda pair: numbers.index(pair[1]) == pair[0], indexed_numbers)
unique = map(lambda pair: pair[1], unique_pairs)
result = sorted(unique)
print(result)

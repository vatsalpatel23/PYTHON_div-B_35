numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = list(filter(lambda number: number % 2 == 0, numbers))
odd = list(filter(lambda number: number % 2 != 0, numbers))
print('Even:', even)
print('Odd:', odd)

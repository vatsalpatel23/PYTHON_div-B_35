numbers = [number for number in range(1, 101)]
print('Squares:', [number * number for number in numbers])
print('Cubes:', [number ** 3 for number in numbers])
print('Even:', [number for number in numbers if number % 2 == 0])
print('Odd:', [number for number in numbers if number % 2 != 0])
print('Multiples of 5:', [number for number in numbers if number % 5 == 0])

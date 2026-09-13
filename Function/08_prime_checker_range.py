def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
number = int(input('Enter number: '))
print('Prime:' if is_prime(number) else 'Not prime:', number)
start = int(input('Range start: '))
end = int(input('Range end: '))
print([value for value in range(start, end + 1) if is_prime(value)])

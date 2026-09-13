def to_binary(number):
    return bin(number)[2:]

def to_octal(number):
    return oct(number)[2:]

def to_hexadecimal(number):
    return hex(number)[2:].upper()
number = int(input('Enter a decimal number: '))
print('Binary:', to_binary(number))
print('Octal:', to_octal(number))
print('Hexadecimal:', to_hexadecimal(number))

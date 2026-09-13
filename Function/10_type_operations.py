def perform_operations(first, second):
    if type(first) == int and type(second) == int:
        return (first + second, first * second)
    return (str(first) + str(second), str(first) * int(second) if str(second).isdigit() else 'Cannot multiply')
first = input('Enter first value: ')
second = input('Enter second value: ')
if first.isdigit() and second.isdigit():
    first = int(first)
    second = int(second)
print(perform_operations(first, second))

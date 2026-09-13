items = input('Enter values separated by spaces: ').split()
check_digit = lambda item: item.isdigit()
result = list(map(check_digit, items))
print(result)

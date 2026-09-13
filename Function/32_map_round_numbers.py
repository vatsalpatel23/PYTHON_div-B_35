numbers = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344]
whole_numbers = list(map(lambda number: round(number), numbers))
two_decimals = list(map(lambda number: round(number, 2), numbers))
print('Whole numbers:', whole_numbers)
print('Two decimals:', two_decimals)

items = ['pen', 'book', 'bag', 'scale']
item = input('Enter item to search: ')
if item in items:
    print('Element exists.')
else:
    print('Element does not exist.')

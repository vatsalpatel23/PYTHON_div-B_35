items = []
while True:
    print('1 Add  2 Remove  3 Search  4 Update  5 Sort  6 Display  7 Exit')
    choice = input('Choose: ')
    if choice == '1':
        items.append(input('Item: '))
    elif choice == '2':
        item = input('Item: ')
        if item in items:
            items.remove(item)
    elif choice == '3':
        print('Found' if input('Item: ') in items else 'Not found')
    elif choice == '4':
        old = input('Old item: ')
        if old in items:
            items[items.index(old)] = input('New item: ')
    elif choice == '5':
        items.sort()
    elif choice == '6':
        print(items)
    elif choice == '7':
        break
    else:
        print('Invalid choice')

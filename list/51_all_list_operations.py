items = []
while True:
    print('1 Append 2 Insert 3 Extend 4 Remove 5 Pop 6 Sort 7 Reverse')
    print('8 Count 9 Index 10 Copy 11 Clear 12 Display 13 Exit')
    choice = input('Choose: ')
    if choice == '1':
        items.append(input('Value: '))
    elif choice == '2':
        items.insert(int(input('Position: ')), input('Value: '))
    elif choice == '3':
        items.extend(input('Values separated by spaces: ').split())
    elif choice == '4':
        value = input('Value: ')
        if value in items:
            items.remove(value)
    elif choice == '5':
        print('Removed:', items.pop() if items else 'List is empty')
    elif choice == '6':
        items.sort()
    elif choice == '7':
        items.reverse()
    elif choice == '8':
        print(items.count(input('Value: ')))
    elif choice == '9':
        value = input('Value: ')
        print(items.index(value) if value in items else 'Not found')
    elif choice == '10':
        print('Copy:', items.copy())
    elif choice == '11':
        items.clear()
    elif choice == '12':
        print(items)
    elif choice == '13':
        break

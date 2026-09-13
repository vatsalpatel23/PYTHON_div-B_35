cities = ['Ahmedabad', 'Surat']
while True:
    print('1 Add 2 Display 3 Update 4 Delete 5 Exit')
    choice = input('Choose: ')
    if choice == '1':
        cities.append(input('City: '))
    elif choice == '2':
        print(cities)
    elif choice == '3':
        city = input('Existing city: ')
        if city in cities:
            cities[cities.index(city)] = input('New city: ')
    elif choice == '4':
        city = input('City: ')
        if city in cities:
            cities.remove(city)
    elif choice == '5':
        break

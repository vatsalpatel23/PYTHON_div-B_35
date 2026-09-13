numbers = [int(input('Enter number ' + str(i) + ': ')) for i in range(1, 16)]
even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]
for name, group in [('Even', even), ('Odd', odd)]:
    print(name, 'list:', group)
    if group:
        print('Count:', len(group), 'Sum:', sum(group), 'Max:', max(group), 'Min:', min(group))

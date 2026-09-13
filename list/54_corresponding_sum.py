first = [int(value) for value in input('First list: ').split()]
second = [int(value) for value in input('Second list: ').split()]
if len(first) == len(second):
    third = []
    for index in range(len(first)):
        third.append(first[index] + second[index])
    print(third)
else:
    print('Lists must have equal size.')

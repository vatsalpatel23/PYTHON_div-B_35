def in_range(number, start, end):
    return start <= number <= end
number = int(input('Enter number: '))
start = int(input('Enter range start: '))
end = int(input('Enter range end: '))
print(in_range(number, start, end))

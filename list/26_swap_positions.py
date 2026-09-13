numbers = [10, 20, 30, 40, 50]
first = int(input('First position: '))
second = int(input('Second position: '))
numbers[first], numbers[second] = (numbers[second], numbers[first])
print(numbers)

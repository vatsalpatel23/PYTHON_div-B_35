marks = [78, 85, 62, 91, 74, 88, 69, 95, 80, 72]
marks.insert(2, 76)
marks.remove(62)
marks[0] = 82
marks.sort()
print('Sorted:', marks)
marks.reverse()
print('Reversed:', marks)
print('Highest:', max(marks))
print('Lowest:', min(marks))
print('Average:', sum(marks) / len(marks))

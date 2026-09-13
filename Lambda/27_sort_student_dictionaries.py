students = [{'name': 'Amit', 'marks': 78}, {'name': 'Bina', 'marks': 92}, {'name': 'Dax', 'marks': 85}]
result = sorted(students, key=lambda student: student['marks'])
print(result)

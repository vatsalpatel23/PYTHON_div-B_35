students = [{'name': 'Amit', 'age': 25}, {'name': 'Bina', 'age': 22}, {'name': 'Dax', 'age': 25}]
result = sorted(students, key=lambda student: (student['age'], student['name']))
print(result)

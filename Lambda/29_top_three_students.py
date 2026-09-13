students = [('Amit', 78), ('Bina', 92), ('Dax', 85), ('Diya', 95)]
result = sorted(students, key=lambda student: student[1], reverse=True)[:3]
print(result)

students = [('Amit', 78), ('Bina', 35), ('Dax', 85), ('Diya', 28)]
passed = filter(lambda student: student[1] >= 35, students)
result = sorted(passed, key=lambda student: student[1])
print(result)

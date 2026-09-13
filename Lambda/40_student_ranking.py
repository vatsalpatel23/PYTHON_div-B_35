students = [('Amit', 78), ('Bina', 92), ('Dax', 85), ('Diya', 95)]
ranking = sorted(students, key=lambda student: student[1], reverse=True)
for position, student in enumerate(ranking, 1):
    print(position, student[0], student[1])

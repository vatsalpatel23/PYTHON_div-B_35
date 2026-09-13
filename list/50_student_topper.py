students = [[101, 'Aarav', 82], [102, 'Diya', 91], [103, 'Kabir', 76]]
students.sort(key=lambda student: student[2], reverse=True)
print('Topper:', students[0])
print('Sorted students:', students)

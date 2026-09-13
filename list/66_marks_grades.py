marks = [95, 82, 71, 60, 48, 32]
grades = ['A' if mark >= 90 else 'B' if mark >= 80 else 'C' if mark >= 70 else 'D' if mark >= 60 else 'F' for mark in marks]
print(grades)

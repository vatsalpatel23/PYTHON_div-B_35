"""Program 2.12: sort and filter student records."""
students = [("Aarav", 82), ("Diya", 55), ("Kabir", 91), ("Meera", 67), ("Rohan", 48)]
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
passed_students = list(filter(lambda student: student[1] >= 60, students))
print("Sorted by marks:", sorted_students)
print("Marks >= 60:", passed_students)

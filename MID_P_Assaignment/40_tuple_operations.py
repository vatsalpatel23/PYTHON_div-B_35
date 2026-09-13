"""Program 3.4: tuple operations."""
marks = (72, 85, 91, 68, 79)
print("Marks:", marks)
print("First mark:", marks[0])
print("Slice 1:4:", marks[1:4])
print("Length:", len(marks))
minimum, maximum, average = min(marks), max(marks), sum(marks) / len(marks)
print("Min:", minimum, "Max:", maximum, "Average:", round(average, 2))
try: marks[0] = 100
except TypeError as error: print("Tuple cannot be modified:", error)
updated_marks = list(marks)
updated_marks[0] = 100
marks = tuple(updated_marks)
print("Updated tuple:", marks)

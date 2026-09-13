"""Program 1.11: marks, percentage and average."""

marks = []
for subject in range(1, 6):
    marks.append(float(input("Enter marks for subject " + str(subject) + ": ")))
total = sum(marks)
print("Total:", round(total, 2), "/500")
print("Percentage:", round(total / 5, 2), "%")
print("Average:", round(total / 5, 2))

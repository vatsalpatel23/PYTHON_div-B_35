"""Program 2.10: formatted report card using f-strings."""
student_name, roll_no = "Your Name", "Your Roll No."
marks = [85, 78, 92, 88, 81]
total, percentage = sum(marks), sum(marks) / 5
grade = "A+" if percentage >= 90 else "A" if percentage >= 80 else "B" if percentage >= 70 else "C" if percentage >= 60 else "D" if percentage >= 35 else "Fail"
print(f"{'REPORT CARD':^34}\n{'Name:':15}{student_name}\n{'Roll No.:':15}{roll_no}\n{'Marks:':15}{marks}\n{'Total:':15}{total}/500\n{'Percentage:':15}{percentage:.2f}%\n{'Grade:':15}{grade}")

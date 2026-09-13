"""Program 1.20: star pattern collection."""
rows = 5
print("Right-angled triangle")
for i in range(1, rows + 1): print("*" * i)
print("Inverted triangle")
for i in range(rows, 0, -1): print("*" * i)
print("Diamond")
for i in range(1, rows + 1, 2): print(" " * ((rows - i) // 2) + "*" * i)
for i in range(rows - 2, 0, -2): print(" " * ((rows - i) // 2) + "*" * i)

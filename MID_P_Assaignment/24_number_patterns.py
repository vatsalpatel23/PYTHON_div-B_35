"""Program 1.24: ascending and descending number patterns."""
for row in range(1, 6):
    for number in range(1, row + 1): print(number, end=" ")
    print()
print("Reverse pattern")
for row in range(5, 0, -1):
    for number in range(1, row + 1): print(number, end=" ")
    print()

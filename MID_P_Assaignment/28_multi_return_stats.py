"""Program 2.4: multi-return statistics function."""
def stats(a, b, c):
    return a + b + c, (a + b + c) / 3, min(a, b, c), max(a, b, c)

values = [float(input("Enter number " + str(i) + ": ")) for i in range(1, 4)]
total, average, minimum, maximum = stats(*values)
print("Sum:", total)
print("Average:", round(average, 2))
print("Minimum:", minimum)
print("Maximum:", maximum)

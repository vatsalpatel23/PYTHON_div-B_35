"""Program 1.15: multiplication table."""

number = int(input("Enter a number: "))
for value in range(1, 11):
    print(number, "x", value, "=", number * value)

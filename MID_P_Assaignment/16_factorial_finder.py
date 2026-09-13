"""Program 1.16: factorial using a for loop."""
number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for value in range(2, number + 1):
        fact *= value
    print(number, "! =", fact)

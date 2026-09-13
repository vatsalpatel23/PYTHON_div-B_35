"""Program 1.9: swap two numbers in two ways."""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
original_a, original_b = a, b
print("Before swap: a =", a, ", b =", b)
a, b = b, a
print("Tuple swap: a =", a, ", b =", b)
a, b = original_a, original_b
a = a + b
b = a - b
a = a - b
print("Arithmetic swap: a =", a, ", b =", b)

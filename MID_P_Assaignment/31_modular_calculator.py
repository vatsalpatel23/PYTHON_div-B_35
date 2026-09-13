"""Program 2.7: menu-driven modular calculator."""
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def power(a, b): return a ** b

operations = {"1": ("Add", add), "2": ("Subtract", subtract), "3": ("Multiply", multiply), "4": ("Divide", divide), "5": ("Power", power)}
for key, (name, _) in operations.items(): print(key + ".", name)
choice = input("Choose an operation: ")
if choice in operations:
    a, b = float(input("First number: ")), float(input("Second number: "))
    try: print("Result:", operations[choice][1](a, b))
    except ZeroDivisionError: print("Cannot divide by zero.")
else: print("Invalid choice.")

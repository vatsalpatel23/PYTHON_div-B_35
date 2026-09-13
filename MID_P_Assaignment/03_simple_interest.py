"""Program 1.3: simple interest calculator."""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate (%): "))
time = float(input("Enter time (years): "))
interest = principal * rate * time / 100
print("Simple interest:", round(interest, 2))
print("Total amount:", round(principal + interest, 2))

"""Program 1.13: classify a number."""

number = int(input("Enter an integer: "))
sign = "positive" if number > 0 else "negative" if number < 0 else "zero"
parity = "even" if number % 2 == 0 else "odd"
divisible = "is" if number % 5 == 0 else "is not"
print("The number is", sign + ",", parity + ", and", divisible, "divisible by 5.")

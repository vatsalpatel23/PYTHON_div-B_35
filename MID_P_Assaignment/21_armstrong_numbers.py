"""Program 1.21: Armstrong number checker and finder."""
def is_armstrong(number):
    digits = str(number)
    return number == sum(int(digit) ** len(digits) for digit in digits)

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
print("Armstrong numbers from 1 to 999:")
print(*[n for n in range(1, 1000) if is_armstrong(n)])

"""Program 1.19: reverse and test a number."""
original = int(input("Enter a non-negative number: "))
if original < 0:
    print("Please enter a non-negative number.")
else:
    number, reverse = original, 0
    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    print("Reversed number:", reverse)
    print("It is a palindrome." if original == reverse else "It is not a palindrome.")

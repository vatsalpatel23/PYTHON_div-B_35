"""Program 1.7: extract digits of a three-digit number."""

number = int(input("Enter a three-digit number: "))
if 100 <= abs(number) <= 999:
    number = abs(number)
    hundreds, remainder = divmod(number, 100)
    tens, units = divmod(remainder, 10)
    print("Hundreds:", hundreds)
    print("Tens:", tens)
    print("Units:", units)
    print("Sum:", hundreds + tens + units)
    print("Product:", hundreds * tens * units)
else:
    print("Please enter exactly a three-digit number.")

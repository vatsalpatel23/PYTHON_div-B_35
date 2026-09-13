"""Program 2.2: prime checker function."""
def is_prime(number):
    if number < 2: return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0: return False
    return True

roll_no = int(input("Enter your roll number: "))
for number in range(roll_no, roll_no + 11):
    print(number, ":", "Prime" if is_prime(number) else "Not prime")

"""Program 1.17: check a prime and list primes."""
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

number = int(input("Enter N: "))
if is_prime(number):
    print(number, "is prime.")
else:
    print(number, "is not prime.")
print("Primes from 2 to N:", *[n for n in range(2, number + 1) if is_prime(n)])

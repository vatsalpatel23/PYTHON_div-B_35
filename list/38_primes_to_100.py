primes = []
for number in range(2, 101):
    prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            break
    if prime:
        primes.append(number)
print(primes)

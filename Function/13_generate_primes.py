def generate_primes(count):
    primes = []
    number = 2
    while len(primes) < count:
        prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                prime = False
                break
        if prime:
            primes.append(number)
        number += 1
    return primes
count = int(input('How many prime numbers? '))
print(generate_primes(count))

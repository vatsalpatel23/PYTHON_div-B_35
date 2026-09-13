numbers = list(range(1, 21))
result = []
for number in numbers:
    prime = number >= 2
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
    if not prime:
        result.append(number)
print(result)

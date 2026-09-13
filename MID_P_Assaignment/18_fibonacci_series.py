"""Program 1.18: Fibonacci series with while loop."""
terms = int(input("How many terms? "))
a, b, count = 0, 1, 0
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

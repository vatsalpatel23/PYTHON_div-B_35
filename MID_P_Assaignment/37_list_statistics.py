"""Program 3.1: list statistics."""
count = int(input("How many numbers? "))
numbers = [float(input("Number " + str(i) + ": ")) for i in range(1, count + 1)]
if numbers:
    print("List:", numbers)
    print("Sorted:", sorted(numbers))
    print("Reversed:", list(reversed(numbers)))
    print("Max:", max(numbers))
    print("Min:", min(numbers))
    print("Sum:", sum(numbers))
    print("Average:", round(sum(numbers) / len(numbers), 2))
else: print("No numbers entered.")

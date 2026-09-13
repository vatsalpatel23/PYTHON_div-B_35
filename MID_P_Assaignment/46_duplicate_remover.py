"""Program 3.10: remove duplicates and compare lists."""
count = int(input("How many numbers in list 1? "))
list_one = [int(input("Number " + str(i) + ": ")) for i in range(1, count + 1)]
list_two = [int(value) for value in input("Enter list 2 numbers separated by spaces: ").split()]
frequency = {}
for number in list_one: frequency[number] = frequency.get(number, 0) + 1
print("Without duplicates:", list(set(list_one)))
print("Only in list 1:", list(set(list_one) - set(list_two)))
print("Frequency:", frequency)

"""Program 3.3: list comprehension examples."""
sentence = "Python makes programming simple and enjoyable"
print("Squares:", [number ** 2 for number in range(1, 21)])
print("Even numbers:", [number for number in range(1, 51) if number % 2 == 0])
print("Long words:", [word for word in sentence.split() if len(word) > 4])
print("Odd cubes:", [number ** 3 for number in range(1, 16) if number % 2 != 0])

"""Program 1.5: rectangle and circle calculations."""

from math import pi

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
print("Rectangle area:", round(length * breadth, 2))
print("Rectangle perimeter:", round(2 * (length + breadth), 2))
print("Circle area (radius = length):", round(pi * length ** 2, 2))

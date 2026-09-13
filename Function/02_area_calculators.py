from math import pi

def rectangle_area(width, length):
    return width * length

def triangle_area(height, base):
    return 0.5 * height * base

def circle_area(radius):
    return pi * radius * radius
print('Rectangle:', rectangle_area(5, 8))
print('Triangle:', triangle_area(4, 6))
print('Circle:', round(circle_area(3), 2))
